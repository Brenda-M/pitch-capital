from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import current_app
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20), unique=True, nullable =False)
  email = db.Column(db.String(120), unique=True, nullable =False)
  image_file = db.Column(db.String(120), nullable =False, default='default.jpg')
  password = db.Column(db.String(60), nullable =False)
  pitch = db.relationship('Pitch', backref='author', lazy='dynamic')
  comments = db.relationship('Comment', backref='author', lazy='dynamic')
  upvotes = db.relationship('Upvote', backref = 'author', lazy='dynamic')

  def get_reset_token(self, expires_sec=1800):
    s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    return s.dumps({'user_id': self.id}).decode('utf-8')
  
  @staticmethod
  def verify_reset_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
      user_id = s.loads(token)['user_id']
    except:
      return None
    return User.query.get(user_id)


  def __repr__(self):
    return(f"User('{self.username}', '{self.email}', '{self.image_file}')")

class Pitch(db.Model):

  __tablename__ = "pitches"

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(200), nullable = False)
  pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
  upvotes = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    
  def __repr__(self):
    return(f"User('{self.title}', '{self.pub_date}')")

class Comment (db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer,primary_key = True)
  content = db.Column(db.Text, nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id') ,  nullable=False)

  def __repr__(self):
    return(f"User('{self.content}', '{self.date_posted}')")

class Upvote(db.Model):

  __tablename__ = 'upvotes'

  id = db.Column(db.Integer, primary_key=True)
  upvote = db.Column(db.Integer, default=0)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  pitch_id = db.Column(db.Integer, db.ForeignKey('post.id'))

  def save_upvotes(self):
    db.session.add(self)
    db.session.commit()

  def add_upvotes(cls,id):
    upvote_pitch = Upvote(user = current_user, pitch_id=id)
    upvote_pitch.save_upvotes()

    
  @classmethod
  def get_upvotes(cls,id):
    upvote = Upvote.query.filter_by(pitch_id=id).all()
    return upvote

  @classmethod
  def get_all_upvotes(cls,pitch_id):
    upvotes = Upvote.query.order_by('id').all()
    return upvotes

  def __repr__(self):
    return f'{self.user_id}:{self.pitch_id}'

