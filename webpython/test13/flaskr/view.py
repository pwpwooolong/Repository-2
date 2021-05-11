from flaskr import app	# flaskr是專案裡的資料夾名稱
from flaskr import db
from flask import render_template, flash
from flaskr.model import UserRegister
from flaskr.form import FormRegister, FormLogin

db.init_app(app)
with app.app_context():
   db.create_all()

@app.route('/index')
def index():
   return "This is index!"
   
@app.route('/register', methods=['GET', 'POST'])
def register():
   form = FormRegister()
   if form.validate_on_submit():
      user = UserRegister(
      username = form.username.data,
      email = form.email.data,
      password = form.password.data
      )
      db.session.add(user)
      db.session.commit()
      return '註冊成功！'
   return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = FormLogin()
   if form.validate_on_submit():
       user = UserRegister.query.filter_by(email=form.email.data).first()
       if user:
           #  當使用者存在資料庫內再核對密碼是否正確。
           if user.check_password(form.password.data):
               return '歡迎'
           else:
               #  如果密碼驗證錯誤，就顯示錯誤訊息。
               flash('Wrong Email or Password')
       else:
           #  如果資料庫無此帳號，就顯示錯誤訊息。
           flash('Wrong Email or Password')
   return render_template('login.html', form=form)

@app.route('/logout')
def logout():
   return 'Here is Logout'

@app.route('/userinfo')
def userinfo():
   return 'Here is UserINFO'