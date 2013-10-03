# coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))
MAX_CONTENT_LENGTH = 5 * 1024 * 1024 # 5 Megabytes

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/dbname?charset=utf8'

RECAPTCHA_PUBLIC_KEY = 'recaptcha public key'
RECAPTCHA_PRIVATE_KEY = 'recaptcha private key'

COOKIES_MAX_AGE = 2592000
CSRF_ENABLED = True
SECRET_KEY = 'changeme'
SITE_NAME = u'Site Name'
SERVER_NAME = 'localhost:5000'