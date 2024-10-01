# models.py will contain all the database models ( how we interact with the database )
# we use Flask-SQLAlchemy to create a python class which represents some kind of entry/row for the database/some kind of a table and we define the different columns and data that the class/objects will be 

from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)


# define a function that can take all the
# attributes in the object above and convert
# it into a python dictionary which we can
# then convert into json, something that we
# can pass from our API

# the way we communicate in API is using something known as json which looks like a python dictionary. We will be passing json back and forth so that API will return json and we will send json to the API for creating our different objects

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }