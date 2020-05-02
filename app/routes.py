from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb7a5bab1e32eb33a9fb58c3294107b4'




@app.route('/')
@app.route('/home')
def index():

  title = "Welcome to PitchCapital"

  return render_template('index.html', title=title)

@app.route('/about')
def about():

  title = "About PitchCapital"

  return render_template('about.html', title=title)

@app.route('/register')
def register():
  form = RegistrationForm()
  return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
  app.run(debug=True)
