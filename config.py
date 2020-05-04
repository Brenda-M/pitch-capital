import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Bm19952810@localhost/pitchapp'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME  = os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The parent configuration class with general configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}