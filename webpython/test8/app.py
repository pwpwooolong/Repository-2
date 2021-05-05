# app.py
import json
import db
import sqlite3 as sql
from flask import Flask, request, render_template

DB = db.DatabaseDriver()

app = Flask(__name__)

def success_response(data, code=200):
   return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
   return json.dumps({"success": False, "error": message}), code
   

@app.route("/tasks/")
def get_tasks():
     return success_response(DB.get_all_tasks())

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         addr = request.form['addr']
         city = request.form['city']
         pin = request.form['pin']
         DB.insert_task_table(name, addr, city, pin)
         msg = "新增成功"

      except Exception as e:
         print(e)
         msg = "新增失敗"
         
      finally: 
         return render_template("result.html", msg=msg)
    

@app.route('/list')
def list():
    rows = DB.get_all_tasks()
    return render_template("list.html", rows=rows)