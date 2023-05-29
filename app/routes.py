from flask import render_template, flash, abort
from app import app, db
from app.models import Listing
from app.openai_client import get_summary

SUMMARIES = dict()

@app.route('/')
@app.route('/home')
def home():
    listings = Listing.query.limit(5).all()
    return render_template('home.html', jobs=listings)

@app.route('/listings')
@app.route('/jobs')
def all_listings():
    listings = Listing.query.all()
    return render_template('listings.html', listings=listings)

@app.route('/listing/<slug>')
def listing(slug):
    listing = Listing.query.filter_by(slug=slug).first()
    if listing is not None:
        return render_template('listing.html', job=listing)
    abort(404)

@app.route('/summarize/<slug>')
def summary(slug):
    listing = Listing.query.filter_by(slug=slug).first()
    if listing is not None:
        if listing.title not in SUMMARIES:
            summary = get_summary(
                listing.title,
                listing.team_description,
                listing.role_description,
                listing.benefits_compensation,
                listing.responsibilities,
                f"{listing.salary}{listing.currency}",
            )
            SUMMARIES[listing.title] = summary
            return summary
        else:
            return SUMMARIES[listing.title]
    abort(404)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
