
from flask import Blueprint, render_template 
from app.models import Pitch

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():

  title = "Welcome to PitchCapital"
  pitches = Pitch.query.all()

  return render_template('index.html', title=title, pitches=pitches)

