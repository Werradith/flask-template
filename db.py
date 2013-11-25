from flask.ext.sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

def get_password_hash(pwd):
    import hashlib
    return hashlib.md5((pwd + app.config['SECRET_KEY']).encode('utf-8')).hexdigest()

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(32))
    email = db.Column(db.String(70))
    register_date = db.Column(db.DateTime())
    register_ip = db.Column(db.String(15))
    last_login = db.Column(db.DateTime())
    last_ip = db.Column(db.String(15))

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    db.Model.metadata.create_all()