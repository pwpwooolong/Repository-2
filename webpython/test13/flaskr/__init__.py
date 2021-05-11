from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
from flask_bcrypt import Bcrypt
pjdir = os.path.abspath(os.path.dirname(__file__))

# 專案環境變數
app = Flask(__name__,template_folder="templates")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
   os.path.join(pjdir, 'data.sqlite')
app.config['SECRET_KEY'] = os.urandom(24)

# 套件參數初始化
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#  載入專案中的route頁面
from flaskr import view