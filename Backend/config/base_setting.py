#公用配置
DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENCODING = "utf8mb4"
SQLALCHEMY_DATABASE_URI = "mysql://root:songzihan@localhost/smart_application?charset=utf8"

SECRET_KEY = "songzihan"
# 不禁用csrf会报错
WTF_CSRF_ENABLED = False

# 注册邀请码
REGISTER_KEY = 'yysongzihan'
# 登录加密值,正式使用应该放在secret 文件夹
SECRET_WORD = 'ifjasdfbnkjadfgbnio3294i239ru'

DOMAIN = {
    "www":"http://localhost:5000"
}
