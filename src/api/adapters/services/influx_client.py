from influxdb import InfluxDBClient

from api.common.config import config


class InfluxClient:

    def __init__(self):
        self._db_client = InfluxDBClient(host=config['DB_HOST'], port=config['DB_PORT'], pool_size=10)

    def write(self, data, db_name, protocol: str, batch_size: int = 10000, time_precision: str = 's'):
        self._db_client.switch_database(db_name)
        self._db_client.write_points(data, batch_size=batch_size, protocol=protocol, time_precision=time_precision)

    def create_database(self, db_name):
        self._db_client.create_database(db_name)
