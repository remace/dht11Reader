#! /usr/bin/env python
from flask_sqlalchemy import SQLAlchemy
import datetime

from .views import app


db = SQLAlchemy(app)


class Statement(db.Model):
    __tablename__ = "statements"

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    stated_at = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, temp, hum):
        self.temperature = temp
        self.humidity = hum
        self.created_at = datetime.now()


db.create_all()
