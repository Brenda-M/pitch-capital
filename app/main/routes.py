
from flask import Blueprint, render_template 
from app.models import Post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():

  title = "Welcome to PitchCapital"
  posts = Post.query.all()
  return render_template('index.html', title=title, posts=posts)

@main.route('/about')
def about():

  title = "About PitchCapital"

  return render_template('about.html', title=title)

