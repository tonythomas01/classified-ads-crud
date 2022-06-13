import os
import tempfile

import pytest

from classified_ads_crud.app import create_app
from config import Config


@pytest.fixture
def client():
    db_fd, random_file = tempfile.mkstemp()
    Config.SQLALCHEMY_DATABASE_URI = f"sqlite:///{random_file}"

    app = create_app()
    app.config.from_object(Config)

    with app.test_client() as client:
        with app.app_context():
            from classified_ads_crud.database import init_db

            init_db()
        yield client
    os.close(db_fd)
    os.unlink(random_file)


@pytest.fixture(scope="session")
def runner(app):
    return app.test_cli_runner()
