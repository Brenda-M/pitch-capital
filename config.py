import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Bm19952810@localhost/pitchapp_test'

class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The parent configuration class with general configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_BLUE_URL")

class DevConfig(Config):
  '''
  Development configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Bm19952810@localhost/pitchapp'
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test': TestConfig
}