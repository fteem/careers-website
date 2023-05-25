import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy_utils import CurrencyType, Currency
from db.connection import Base

class Listing(Base):
    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=False)
    slug = Column(String(120), unique=True)
    location = Column(String(120), unique=False)
    salary = Column(Integer, unique=False)
    currency = Column(CurrencyType)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, title=None, slug=None, location=None, salary=None, currency=Currency('USD')):
        self.title = title
        self.slug = slug
        self.location = location
        self.salary = salary
        self.currency = currency

    def __repr__(self):
        return f'<Listing {self.title!r}>'
