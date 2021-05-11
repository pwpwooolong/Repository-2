from flaskr import db, bcrypt
class UserRegister(db.Model):
   """記錄使用者資料的資料表"""
   __tablename__ = 'UserRegister'
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   email = db.Column(db.String(80), unique=True, nullable=False)
   password_hash = db.Column(db.String(128), nullable=False)

   @property
   def password(self):
       raise AttributeError('password is not a readable attribute')

   @password.setter
   def password(self, password):
       self.password_hash = bcrypt.generate_password_hash(
           password).decode('utf8')
   def check_password(self, password):
      return bcrypt.check_password_hash(self.password_hash, password)
