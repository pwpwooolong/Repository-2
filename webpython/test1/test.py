from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/hello')
# def hello():
#     return 'Hello!'

# @app.route('/hello/<name>')
# def hello2(name):
#     return 'Hello, {}!'.format(name)

# @app.route('/hello', defaults={'name': 'Someone'})
# @app.route('/hello/<name>')
# def hello3(name):
#     return 'Hello, {}!!'.format(name)

# @app.route('/', methods=['POST', 'GET'])
# def hello_world2():
#     return 'Hello, World!!!'

# @app.route('/form')
# def form():
#     return '''
#         <form method="POST" action="/process">
#             <label>Input Name: <input type="text" name="name"></label>
#             <input type="submit" value="Submit">
#         </form>
#     '''

# @app.route('/process', methods=['POST'])
# def post_form():
#     name = request.form['name']
#     return 'Hello, {}!'.format(name)

# @app.route('/')
# def index():
#     return '<h1>Hello, world!</h1>'

