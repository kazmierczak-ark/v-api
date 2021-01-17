from influxdb_client import InfluxDBClient, WriteOptions

from api.common.config import config


class InfluxClient:

    def __init__(self):
        self._db_client = InfluxDBClient(url=f"http://{config['DB_HOST']}:{config['DB_PORT']}", token="", org='-',
                                         pool_size=10)

    def write(self, data, bucket, batch_size: int = 10000):
        write_client = self._db_client.write_api(write_options=WriteOptions(batch_size=batch_size))
        write_client.write(bucket=bucket, record=data)

        write_client.close()
