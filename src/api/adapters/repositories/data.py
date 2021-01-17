from api.adapters.services.influx_client import InfluxClient
from api.business_logic.models.data_series import DataSeries


class DataRepository:
    bucket = 'v_timeseries'

    def __init__(self):
        self._influxdb_client = InfluxClient()

    def add(self, data: DataSeries):
        self._influxdb_client.write(data.to_point(), bucket=self.bucket)
