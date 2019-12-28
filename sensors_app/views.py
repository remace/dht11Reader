#! /usr/bin/env python
from flask import Flask, render_template
from . import models


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    temperature = 27.5
    humidity = 45
    return render_template('pages/home.html', temperature=temperature, humidity=humidity)


@app.route('/stats')
def stats():
    posts = models.Statement.query.all()
    if posts != []:
        return render_template('pages/stats.html', posts=posts)
    else:
        return render_template("errors/no_stats_to_show.html"), 404


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404
