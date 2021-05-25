import os

class Config:
    SECRET_KEY = 'ab3dc1078301068d5b'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_DEBUG = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
