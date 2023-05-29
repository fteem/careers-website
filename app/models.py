import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy_utils import CurrencyType, Currency

from app import db

class Listing(db.Model):
    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=False)
    slug = Column(String(120), unique=True)
    location = Column(String(120), unique=False)
    salary = Column(Integer, unique=False)
    currency = Column(CurrencyType)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    team_description = Column(Text)
    role_description = Column(Text)
    responsibilities = Column(Text)
    benefits_compensation = Column(Text)

    def __init__(self, title=None, slug=None, location=None, salary=None, currency=Currency('USD'), team_description=None, role_description=None, responsibilities=None, benefits_compensation=None):
        self.title = title
        self.slug = slug
        self.location = location
        self.salary = salary
        self.currency = currency
        self.team_description = team_description
        self.role_description = role_description
        self.responsibilities = responsibilities
        self.benefits_compensation = benefits_compensation

    def __repr__(self):
        return f'<Listing {self.title!r}>'
