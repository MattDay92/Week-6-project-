from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String, nullable=False)
    details = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, name, img_url, details):
        self.name = name
        self.img_url = img_url
        self.details = details

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
