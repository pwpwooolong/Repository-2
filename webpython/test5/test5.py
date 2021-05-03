from flask import Flask, request, make_response, render_template, session, url_for, redirect
import os
app = Flask(__name__)

app.secret_key = os.urandom(24)
@app.route('/')
def index():
    if 'username' in session:
        username=session['username']
        return '登入名稱:'+username+'<br>'+"<b><a href='/logout'>點此登出</a></b>"
    return "您尚未登入<br><a href='/login'>"+"點此登入</a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    print(session)
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    print(session)
    return redirect(url_for('index'))