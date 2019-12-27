from flask import Flask, render_template
from mocks import Mocks

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/stats')
def stats():
    posts = Mocks.all()
    return render_template('pages/stats.html',posts = posts)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == "__main__":
    app.run(debug = True, port=5000)