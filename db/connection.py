from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db.url import db_url

engine = create_engine(
        db_url,
        connect_args={
            "ssl": {
                "ssl_ca": "/etc/ssl/cert.pem"
            }
        },
        echo=True
    )

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models.listing
    Base.metadata.create_all(bind=engine)
