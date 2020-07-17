from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from application import db
from libs.AWS_S3_Manage import S3
from libs.auth import login_required, jwt_login
from libs.date_helper import getCurrentTime
from libs.return_data_helper import return_JSON
from libs.wtf_helper import Register, Login
from models.user import User

api = Blueprint("api", __name__)

@api.route('/user_info',methods=["GET"],endpoint='/user_info')
@login_required
def user_info(power,username):
    return_data = {
        "code": 200,
        "msg": 'success get info',
        "data":{
            "username": username,
            "role": power
        }
    }
    return return_data

@api.route('/',methods=["GET"],endpoint='/')
@login_required
def homepage(power,username):
    """
    根据用户权限和用户名返回s3中存储桶中的用户信息
    :param power: 用户权限
    :param username: 用户名
    :return: return_data
    """
    s3 = S3(username)
    print(s3.get_bucket_info())
    return_data = {
        "code":200,
        "msg":'success get res',
        "data": {
            "bucket_info":s3.get_bucket_info(),
            "role": power
        }
    }
    return return_data

@api.route('/upload',methods=["POST"],endpoint='/upload')
@login_required
def upload(power,username):
    s3 = S3(username)
    # 下面应该判断权限

    # 上传文件
    print(request.files['file'])

    # file = request.files['file']
    # print(file.filename)
    # if s3.upload_file(file,'test/'):
    #     print('upload success')
    # else:
    #     print('upload failed')


