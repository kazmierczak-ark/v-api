import pytest
from connexion import FlaskApp

from api.resources.exceptions import set_error_handlers


@pytest.fixture(scope="session")
def app_client():
    # TODO prepare db step which also needs to be its own fixture

    app = FlaskApp(__name__, specification_dir="../../api")

    app.add_api('swagger.yaml', validate_responses=True, options={'swagger_ui': True})
    set_error_handlers(app)

    yield app.app.test_client()
