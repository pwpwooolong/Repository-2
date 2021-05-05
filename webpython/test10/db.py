import os
import json
import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 建立關聯資料關係
association_table = db.Table(
   'association',
   db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
   db.Column('category_id',
 db.Integer, db.ForeignKey('category.id')),
)

class Task(db.Model):
   __tablename__ = 'task'		# table 代稱
   id = db.Column(db.Integer, primary_key=True)
   description = db.Column(db.String, nullable=False)
   done = db.Column(db.Boolean, default = False, nullable=False)
   subtasks = db.relationship('Subtask', cascade='delete')
   # cascade 若task刪除，則一并刪除

   categories = db.relationship('Category', secondary=association_table, back_populates='tasks')
   # 建立多對多關係


   def __init__(self, **kwargs):
       self.description = kwargs.get('description')
       self.done = kwargs.get('done')

   def serialize(self):
       return {# Hint: 記得每個變數都要加上self
           "id": self.id,
           "description": self.description,
           "done": self.done,
           "subtasks": [s.serialize() for s in self.subtasks],
           "categories": [c.serialize() for c in self.categories]
			# 加入這兩個欄位的取值
       }

class Subtask(db.Model):
   __tablename__ = 'subtask'	# table 代稱
   id = db.Column(db.Integer, primary_key=True)
   description = db.Column(db.String, nullable=False)
   done = db.Column(db.Boolean, nullable=False)
   task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
  
   def __init__(self, **kwargs):
       self.description = kwargs.get('description')
       self.done = kwargs.get('done')
       self.task_id = kwargs.get('task_id')
   def serialize(self):   
       return {       
           "id": self.id,       
           "description": self.description,       
           "done": self.done }

class Category(db.Model):
   __tablename__ = 'category'
   id = db.Column(db.Integer, primary_key=True)
   description = db.Column(db.String, nullable=False)
   color = db.Column(db.String, nullable=False)
   tasks = db.relationship('Task', secondary=association_table, back_populates = 'categories')
	# 建立多對多關係
   
   def __init__(self, **kwargs):
       self.description = kwargs.get('description')
       self.color = kwargs.get('color')

   def serialize(self):   
       return {       
           "id": self.id,       
           "description": self.description,       
           "color": self.color }







# # From: https://goo.gl/YzypOI
# def singleton(cls):
#     instances = {}

#     def getinstance():
#         if cls not in instances:
#             instances[cls] = cls()
#         return instances[cls]

#     return getinstance

# # Only <=1 instance of the database driver
# # exists within the app at all times
# DatabaseDriver = singleton(DatabaseDriver)