from application import db
from libs.date_helper import getCurrentTime


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(25), nullable=False, unique=True)
    _login_pwd = db.Column(db.String(150), nullable=False)
    # status 管理用户账号是否可用
    status = db.Column(db.Integer, nullable=False, server_default="1")
    # power 为用户权限，默认值为 "admin"-管理员 ;"teacher"-教师级用户;"student"-学生级用户
    power = db.Column(db.String(25), nullable=True)
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())




# db.create_all()
