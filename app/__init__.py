from flask import Flask
from dotenv import load_dotenv
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(
        app,
        engine_options={
            'connect_args': {
                "ssl": {
                    "ssl_ca": "/etc/ssl/cert.pem"
                }
            }
        }
    )
migrate = Migrate(app, db)

# Models must be imported after the database and migration
# are defined as they reference the database
from app import models
from app import routes
