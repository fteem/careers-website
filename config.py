import os
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

load_dotenv()

db_config = dict(
    drivername='mysql+pymysql',
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_DATABASE"),
    query={'charset': 'utf8mb4'}
)

class Config(object):
    SQLALCHEMY_DATABASE_URI = URL.create(**db_config)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
