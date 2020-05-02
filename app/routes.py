from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post



@app.route('/')
@app.route('/home')
def index():

  title = "Welcome to PitchCapital"

  return render_template('index.html', title=title)

@app.route('/about')
def about():

  title = "About PitchCapital"

  return render_template('about.html', title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for { form.username.data}!', 'success')
    return redirect(url_for('index'))
  return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash(f'You have been logged in', 'success')
      return redirect(url_for('index'))
    else:
      flash('Login Unsuccessful. Please check email and password', 'success')

  return render_template('login.html', title='Login', form=form)

