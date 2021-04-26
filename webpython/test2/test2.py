from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loop')
@app.route('/loop/<int:n>')
def loop(n=3):
    return render_template('loop.html', n=n)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)