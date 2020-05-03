from flask import render_template, url_for, flash, redirect
from app import app, bcrypt, db
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, current_user,logout_user



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
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email = form.email.data, password = hashed_password)
    db.session.add(user)
    db.session.commit()
    flash(f'Hello { form.username.data}, Your Account was created succesfully! You are now able to log in', 'success')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      return redirect(url_for('index'))   
    else:
      flash('Login Unsuccessful. Please check email and password', 'danger')

  return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect (url_for('index'))

