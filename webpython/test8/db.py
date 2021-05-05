# db.py
import os
import sqlite3


class DatabaseDriver(object):
    """
    Task APP 的資料方法
    處理資料庫的讀＆寫
    """
    def __init__(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        self.create_task_table()

    def create_task_table(self):
       try:
           self.conn.execute(
               """
                CREATE TABLE students(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                addr TEXT,
                city TEXT,
                pin TEXT)
               """
           )
       except Exception as e:
           print(e)
    
    def get_all_tasks(self):
       cursor = self.conn.execute(
           """
           SELECT * FROM students;
           """
       )
       tasks = []
       for row in cursor:
           tasks.append({"name": row[0],
                       "addr": row[1],
                       "city": row[2],
                       "pin": row[3]})
       return tasks

    def insert_task_table(self, name, addr, city, pin):
       cursor = self.conn.cursor()
       cursor.execute(
           "INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?);",(name, addr, city, pin)
       )
       self.conn.commit()
       return cursor.lastrowid


# From: https://goo.gl/YzypOI
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


# Only <=1 instance of the database driver
# exists within the app at all times
DatabaseDriver = singleton(DatabaseDriver)
