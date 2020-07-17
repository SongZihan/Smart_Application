from datetime import datetime, timedelta

import jwt
from flask import request

from config.base_setting import SECRET_WORD
from libs.return_data_helper import return_JSON


def jwt_login(username,power):
    """
    该函数在接收登录表单的数据之后返回加密的jwt token
    :param
        username: 用户名
        power: 用户权限
    :return: jwt token
    """
    now = datetime.utcnow()
    # 设置6小时后过期
    exp_datetime = now + timedelta(hours=6)

    encoded_jwt = jwt.encode({
        'username': username,
        # exp是到期时间
        'exp': exp_datetime,
        # 权限
        'power':power
    }, SECRET_WORD, algorithm='HS256')

    return encoded_jwt.decode("utf-8")


def login_required(func):
    def wrapper(*args, **kw):
        # 测试token,从header中获取接收的token，并使用UTF-8进行编码，否则无法使用jwt.decode
        try:
            token = request.headers.get('Authorization', default=None).encode('utf-8')
            decode_token = jwt.decode(token,SECRET_WORD, algorithms=['HS256'])
        except Exception as err:
            return return_JSON(401,'you need login~',str(err))
        else:
            # 将数值型的时间转换为datatime类型以比较 https://blog.csdn.net/weixin_41789707/article/details/83009235
            jwt_time = datetime.fromtimestamp(decode_token['exp'])
            if jwt_time < datetime.utcnow():
                return return_JSON(402,'your jwt is out of time~')
            else:
                power = decode_token['power']
                username = decode_token['username']
                # msg为视图函数return的参数,将power作为参数传递给视图函数，在视图函数中进行用户鉴权
                """
                视图函数返回:
                    data { "code":200（正常）或401（登录失败）或400（未获授权）或402（token过期）;
                            "msg": 返回信息';
                            "data": 返回数据（字典格式）
                            }
                """
                return_data = func(power,username,*args, **kw)
                # 将视图函数返回值直接发往客户端
                return return_JSON(return_data["code"],return_data["msg"],return_data["data"])


    return wrapper
