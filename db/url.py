import os
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy.engine.url import URL

db_config = dict(
    drivername='mysql+pymysql',
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_DATABASE"),
    query={'charset': 'utf8mb4'}
)

db_url = URL.create(**db_config)
