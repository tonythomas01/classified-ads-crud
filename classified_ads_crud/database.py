from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from flask import current_app

engine = create_engine(current_app.config["SQLALCHEMY_DATABASE_URI"])
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from classified_ads_crud.models.ad import Ad

    Base.metadata.create_all(bind=engine)
