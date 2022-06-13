"""Flask config class."""
import os


class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = True
    DEBUG = True

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:////tmp/test.db"
    )
    SQLALCHEMY_USERNAME = os.environ.get("POSTGRES_USER", "test")
    SQLALCHEMY_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "test")
    SQLALCHEMY_DATABASE_NAME = os.environ.get("POSTGRES_DB", "test")
