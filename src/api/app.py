import connexion

from api.common.db import configure_database
from api.resources import health_check
from api.resources.exceptions import set_error_handlers

configure_database()

app = connexion.FlaskApp(__name__, port=8000)

health_check.register(app)

set_error_handlers(app)

app.add_api('swagger.yaml', validate_responses=True, strict_validation=True,
            options={'swagger_ui': True, 'swagger_url': 'spec'})

if __name__ == '__main__':
    app.run()
