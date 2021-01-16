from api.business_logic.models.data_series import DataSeries


class SaveData:
    def __init__(self, data_repo):
        self._data_repo = data_repo

    def execute(self, body):
        data = DataSeries.create(body)
        self._data_repo.add(data)
        return
