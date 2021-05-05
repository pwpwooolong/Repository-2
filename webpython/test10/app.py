import json
from flask import Flask, request
from db import db
from db import Category, Subtask, Task

# 定義db 名稱
db_filename = "todo.db"
app = Flask(__name__)

# 設定 db config
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# 初始化
db.init_app(app)
with app.app_context():
   db.create_all()

# reponse format
def success_response(data, code=200):
   return json.dumps({"success": True, "data": data}), code
def failure_response(message, code=404):
   return json.dumps({"success": False, "error": message}), code

@app.route("/")
@app.route("/tasks/")
def get_tasks():
   tasks = [t.serialize() for t in Task.query.all()]
   return success_response(tasks)

@app.route("/subtasks/")
def get_subtasks():
   subtask = [s.serialize() for s in Subtask.query.all()]
   return success_response(subtask)

@app.route("/categories/")
def categories():
   category = [c.serialize() for c in Category.query.all()]
   return success_response(category)

@app.route("/tasks/", methods=["POST"])
def create_task():
   body = json.loads(request.data)

   new_task = Task(
       description=body.get('description', ''),
done=body.get('done', False)
# 無法取得數值時，給予初始值避免出錯
   )

   db.session.add(new_task)
   db.session.commit()
   return success_response(new_task.serialize(), 201)

@app.route("/tasks/<int:task_id>/")
def get_task(task_id):
   task = Task.query.filter_by(id=task_id).first()
	# first() 取出查詢到的第一行資料

	# 下面檢查是否沒有取得任何內容
   if task is None:
       return failure_response("Task not found!")
   return success_response(task.serialize())

@app.route("/tasks/<int:task_id>/", methods=["POST"])
def update_task(task_id):
   task = Task.query.filter_by(id=task_id).first()
   if task is None:
       return failure_response("Task not found!")
  
   # 取得新輸入的值
   body = json.loads(request.data)
   task.description = body.get('description', task.description)
   task.done = body.get('done', task.done)

   db.session.commit()
   return success_response(task.serialize())

@app.route("/tasks/<int:task_id>/", methods=["DELETE"])
def delete_task(task_id):
   task = Task.query.filter_by(id=task_id).first()
   if task is None:
       return failure_response("Task not found!")
  
   db.session.delete(task)  
   db.session.commit()
   return success_response(task.serialize())



# @app.route("/tasks/")
# def get_tasks():
#     return success_response(DB.get_all_tasks())


# @app.route("/tasks/", methods=["POST"])
# def create_task():
#     body = json.loads(request.data)
#     description = body["description"]
#     task_id = DB.insert_task_table(description, False)
#     print(task_id)
#     task = DB.get_task_by_id(task_id)
#     print(task)
#     if task is None:
#         return failure_response("Something went wrong while creating task!")
#     return success_response(task, 201)

# @app.route("/tasks/<int:task_id>/")
# def get_task(task_id):
#     task = DB.get_task_by_id(task_id)
#     if task is None:
#         return failure_response("Task not found!")
#     return success_response(task)

# @app.route("/tasks/<int:task_id>/", methods=["POST"])
# def update_task(task_id):
#     body = json.loads(request.data)
#     description = body["description"]
#     done = bool(body["done"])
#     DB.update_task_by_id(task_id, description, done)

#     task = DB.get_task_by_id(task_id)
#     if task is None:
#         return failure_response("Task not found!")
#     return success_response(task)

# @app.route("/mem_manage/", methods=["DELETE"])
# def delete_task():
#     task = DB.get_task_by_id(task_id)
#     if task is None:
#         return failure_response("Task not found!")
#     DB.delete_task_by_id(task_id)
#     return success_response(task)