from flask import Flask, request, make_response, render_template
# import time
app = Flask(__name__)

# from flask import session      ↓ Session應用
# import os
# app.config['SECRET_KEY'] = os.urandom(24)

# @app.route('/get')
# def get():
#     name = session.get('name')
#     return 'session with name "name" is "{}"'.format(name)

# @app.route('/set')
# def set():
#     name = 'KID'
#     session['name'] = name
#     return 'session with name "name" is set to "{}"'.format(name)

# @app.route('/get')       ↓Cookie應用
# def get():
#     name = request.cookies.get('name')
#     return 'cookie with name "name" is "{}"!!!'.format(name)

# @app.route('/set')
# def set():
#     name = 'KID'
#     response = make_response(
#         'cookie with name "name" is set to "{}"!!!'.format(name))
#     response.set_cookie(key='name', value=name, expires=time.time()+6*60)
#     return response

@app.route('/')
def index():
    return render_template('test4.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['userid']
        print('debug')
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome' + name + '</h1>'