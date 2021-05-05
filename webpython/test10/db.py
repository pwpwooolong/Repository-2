import os
import json
import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
   __tablename__ = 'task'		# table 代稱
   id = db.Column(db.Integer, primary_key=True)
   description = db.Column(db.String, nullable=False)
   done = db.Column(db.Boolean, default = False, nullable=False)

   def __init__(self, **kwargs):
       self.description = kwargs.get('description')
       self.done = kwargs.get('done')

   def serialize(self):
       return {
           "id": self.id,
           "description": self.description,
           "done": self.done
			# Hint: 記得每個變數都要加上self
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