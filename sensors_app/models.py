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
    sensor_id = db.Column(db.Integer)

    def __init__(self, temp, hum, sensor_id):
        self.temperature = temp
        self.humidity = hum
        self.sensor_id = sensor_id
        self.created_at = datetime.now()


class Sensor(db.Model):
    __tablename__ = "sensors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(length=50), unique=True, nullable=False)
    reference = db.Column(db.Text(length=50), nullable=False)


db.create_all()
