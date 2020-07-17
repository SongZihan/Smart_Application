from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

from application import db
from libs.auth import jwt_login
from libs.date_helper import getCurrentTime
from libs.return_data_helper import return_JSON
from libs.wtf_helper import Register, Login
from models.user import User



auth = Blueprint("auth", __name__)

@auth.route('/login',methods=["POST"])
def login():
    """
    登录模块
    :return:
     jwt_token token
     username 用户名
     role 用户权限
    """
    form = Login()
    if form.validate():
        user = User.query.filter_by(login_name=form.username.data).first()
        # 使用check_password_hash验证用户密码，其中第一个参数是数据库中查询的用户加密密码，第二个参数是用户输入的密码
        if check_password_hash(user._login_pwd, form.password.data):
            # 通过验证的话就将用户名和权限添加到jwt中返回客户端
            user_power = user.power
            jwt_token = jwt_login(username=form.username.data,power=user_power)

            return return_JSON(200,"login success~~", data={"jwt_token":jwt_token
                                                            })
        else:
            return return_JSON(401,"密码错误")
    else:
        return return_JSON(401,str(form.errors))

@auth.route('/registered',methods=["POST"])
def registered():
    form = Register()
    if form.validate():
        # 将用户信息注册进数据库
        model_user = User()
        model_user.login_name = form.username.data
        # 普通注册用户的权限统一设置为student
        model_user.power = "student"
        # 使用加密方法存储密码
        model_user._login_pwd = generate_password_hash(form.password.data)
        model_user.created_time = model_user.updated_time = getCurrentTime()
        try:
            db.session.add(model_user)
            db.session.commit()
        except Exception as error:
            return return_JSON(501,str(error))
        else:
            return return_JSON(200,"注册成功~~")
    else:
        # 返回表单验证中的错误信息
        return return_JSON(401,str(form.errors))

