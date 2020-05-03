from datetime import datetime
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20), unique=True, nullable =False)
  email = db.Column(db.String(120), unique=True, nullable =False)
  image_file = db.Column(db.String(120), nullable =False, default='default.jpg')
  password = db.Column(db.String(60), nullable =False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def __repr__(self):
    return(f"User('{self.username}', '{self.email}', '{self.image_file}')")

class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(200), nullable = False)
  category = db.Column(db.String(200), nullable = False)
  pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return(f"User('{self.title}', '{self.category}', '{self.date_posted}')")