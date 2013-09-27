from main import app
from flaskext.mongoalchemy import MongoAlchemy
db = MongoAlchemy(app)

# Example
class Author(db.Document):
    name = db.StringField()

class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Author)
    year = db.IntField()