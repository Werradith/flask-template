from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from main import app

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], encoding='utf8', echo=False, connect_args = {'charset' : 'utf8'})
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

#class Sample(Base):
#    __tablename__ = 'sample'
#    __table_args__ = {
#        'mysql_engine': 'InnoDB',
#        'mysql_charset': 'utf8'
#    }
#    id = Column(Integer, primary_key = True)
#    text = Column(String(100))

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)