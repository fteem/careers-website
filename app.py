from flask import Flask, render_template, flash, abort
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Full Stack Engineer',
        'west-timezone': 'PST',
        'east-timezone': 'CET',
        'salary': '€100,000',
        'location': 'Remote'
    },
    {
        'id': 2,
        'title': 'Backend Engineer',
        'west-timezone': 'PST',
        'east-timezone': 'CET',
        'salary': '€100,000',
        'location': 'Remote'
    },
    {
        'id': 3,
        'title': 'UX Designer',
        'west-timezone': 'PST',
        'east-timezone': 'CET',
        'salary': '€120,000',
        'location': 'Remote'
    },
    {
        'id': 4,
        'title': 'iOS Engineer',
        'west-timezone': 'PST',
        'east-timezone': 'CET',
        'salary': '€100,000',
        'location': 'Remote'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', jobs=JOBS)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")
