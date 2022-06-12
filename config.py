"""Flask config class."""
import os


class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = True
    DEBUG = True

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://test:test@0.0.0.0:5401/test"
    )
    SQLALCHEMY_USERNAME = "test"
    SQLALCHEMY_PASSWORD = "test"
    SQLALCHEMY_DATABASE_NAME = "test"
