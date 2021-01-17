from influxdb import InfluxDBClient

from api.common.config import config


class InfluxSetupClient:

    def __init__(self):
        self._db_client = InfluxDBClient(host=config['DB_HOST'], port=config['DB_PORT'], pool_size=10)

    def create_bucket(self, bucket):
        self._db_client.create_database(bucket)
