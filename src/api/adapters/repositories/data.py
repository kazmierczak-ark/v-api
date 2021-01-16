import json

from api.adapters.services.influx_client import InfluxClient
from api.business_logic.models.data_series import DataSeries


class DataRepository:
    db_name = 'v_timeseries'

    def __init__(self):
        self._influxdb_client = InfluxClient()

    def add(self, data: DataSeries):
        data_to_save = data.to_line()
        self._influxdb_client.write(data_to_save, protocol='line', db_name=self.db_name)
