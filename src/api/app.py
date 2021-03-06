import connexion

from api.resources import health_check
from api.resources.exceptions import set_error_handlers
from api.adapters.repositories.data import DataRepository
from api.adapters.services.influx_setup_client import InfluxSetupClient

InfluxSetupClient().create_bucket(DataRepository.bucket)

app = connexion.FlaskApp(__name__, port=8000)

health_check.register(app)

set_error_handlers(app)

app.add_api('swagger.yaml', validate_responses=True, strict_validation=True,
            options={'swagger_ui': True, 'swagger_url': 'spec'})

if __name__ == '__main__':
    app.run()
