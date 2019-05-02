from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
# change the configration
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # migrate 对象需要同时一app, 和db为参数
login = LoginManager(app)
login.login_view = 'login'  # 强制未登陆的用户登陆， 不然显示login_view对应的网页

from app import routes, models  # models 是依赖db的， 如果将这行代码写在上面就会产生循坏依赖