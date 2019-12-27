from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from mocks import Mocks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Statements(db.Model):
    __tablename__ = "statements"

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    stated_at = db.Column(db.DateTime, default=db.func.now())


@app.route('/')
def home():
    temperature = Mocks.DHT11_temp()
    humidity = Mocks.DHT11_hum()
    return render_template('pages/home.html', temperature=temperature, humidity=humidity)


@app.route('/stats')
def stats():
    posts = Statements.query.all()
    if posts != []:
        return render_template('pages/stats.html', posts=posts)
    else:
        return render_template("errors/no_stats_to_show.html"), 404


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
