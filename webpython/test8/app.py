# app.py
import json
import db
import sqlite3 as sql
from flask import Flask, request, render_template, url_for

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

@app.route('/addrec', methods=['POST'])
def addrec():
   con = sql.connect("database.db")
   msg = "新增失敗"
   if request.method == 'POST':
         try:
            name = request.form['name']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            DB.instert_task_table(name, addr, city, pin)
            msg = "新增成功"
         except:
            con.rollback()

   con.close()
   return render_template("result.html", msg=msg)
    

@app.route('/list')
def list():
    rows = DB.get_all_tasks()
    return render_template("list.html", rows=rows)