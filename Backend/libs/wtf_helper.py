# -*- coding: utf-8 -*-
import datetime
from flask_wtf import Form
from wtforms import TextField, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo

from config.base_setting import REGISTER_KEY
from models.user import User



class Login(Form):
    """
    用来提供登录表单验证的功能
    """
    username = StringField("username", validators=[DataRequired(message="请输入用户名"), Length(6, 25)])
    password = PasswordField("password", validators=[DataRequired(message="请输入密码"), Length(6, 25)])

    def validate_username(self, field):
        if not User.query.filter_by(login_name=field.data).first():
            raise ValidationError('没有找到用户名')


class Register(Form):
    """
    用来提供注册表单验证
    """
    username = StringField("username", validators=[DataRequired(message="请输入用户名"), Length(6, 25)])
    password = PasswordField("password", validators=[DataRequired(message="请输入密码"), Length(6, 25)])
    # 需要输入邀请码才能注册
    register_key = PasswordField("register_key", validators=[DataRequired(message="请输入邀请码")])

    def validate_username(self, field):
        if User.query.filter_by(login_name=field.data).first():
            raise ValidationError('用户名已被注册')

    def validate_register_key(self,field):
        if field.data != REGISTER_KEY:
            raise ValidationError('邀请码不正确')
