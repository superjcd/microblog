import os



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    # use postgresql
    SQLALCHEMY_DATABASE_URI = 'postgresql://jiangchaodi:123456@localhost/mydb' #engin://user:passwwd@host:port/dab
    SQLALCHEMY_TRACK_MODIFICATIONS = False