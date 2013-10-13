from flask.ext.sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

#class Sample(db.Model):
#    __tablename__ = 'sample'
#    __table_args__ = {
#        'mysql_engine': 'InnoDB',
#        'mysql_charset': 'utf8'
#    }
#    id = db.Column(db.Integer, primary_key = True)
#    text = db.Column(db.String(100))

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    db.Model.metadata.create_all()