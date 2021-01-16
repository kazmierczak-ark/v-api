from api.adapters.repositories.data import DataRepository
from api.adapters.services.influx_client import InfluxClient


# pseudo migration for setup
def configure_database():
    db_client = InfluxClient()
    db_client.create_database(DataRepository.db_name)
