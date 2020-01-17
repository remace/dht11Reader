#! /usr/bin/env python
from flask import Flask, render_template
from . import models
import Adafruit_DHT

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    sensor = Adafruit_DHT.AM2302
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return render_template('pages/home.html',
                           temperature=temperature,
                           humidity=humidity)


@app.route('/admin/')
def admin():
    sensors = models.Sensor.query.all()
    return render_template('pages/admin.html', sensors=sensors)


@app.route('/stats/')
def stats():
    posts = models.Statement.query.all()
    if posts != []:
        return render_template('pages/stats.html', posts=posts)
    else:
        return render_template("errors/no_stats_to_show.html"), 404


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404
