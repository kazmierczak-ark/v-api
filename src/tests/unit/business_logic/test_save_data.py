import pytest

from api.business_logic.models.common import BadRequestError
from api.business_logic.models.data_series import DataSeries
from api.business_logic.save_data import SaveData
from tests.unit.fixtures.data import valid_data, invalid_data


def test_save_data_with_valid_data_then_call_repo(mocker):
    repo = mocker.Mock()
    bl = SaveData(data_repo=repo)
    bl.execute(valid_data)

    # a bit redundant for a check - if there were more transformations the final state of data passed to repo would be prepared as constant value
    repo.add.assert_called_once_with(DataSeries.create(valid_data))


def test_save_data_with_invalid_data_then_return_bad_request(mocker):
    with pytest.raises(BadRequestError):
        SaveData(mocker.Mock()).execute(invalid_data)
