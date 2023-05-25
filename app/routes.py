from flask import render_template, flash, abort
from app import app
JOBS = [
    {
        'id': 1,
        'slug': 'full-stack-engineer',
        'title': 'Full Stack Engineer',
        'west-timezone': 'PST',
        'east-timezone': 'CET',
        'salary': '€100,000',
        'location': 'Remote'
    },
    {
        'id': 2,
        'slug': 'backend-engineer',
        'title': 'Backend Engineer',
        'west-timezone': 'PST',
        'east-timezone': 'CET',
        'salary': '€100,000',
        'location': 'Remote'
    },
    {
        'id': 3,
        'slug': 'ux-designer',
        'title': 'UX Designer',
        'west-timezone': 'PST',
        'east-timezone': 'CET',
        'salary': '€120,000',
        'location': 'Remote'
    },
    {
        'id': 4,
        'slug': 'ios-engineer',
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

@app.route('/listing/<slug>')
def listing(slug):
    for job in JOBS:
        if job['slug'] == slug:
            return render_template('listing.html', job=job)
    abort(404)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

# @app.teardown_appcontext
# def shutdown_session(exception=None):
    #foo
