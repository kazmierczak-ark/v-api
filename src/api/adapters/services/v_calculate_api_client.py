from v_calculate_api_client.api import aggregate_api

from api.common.config import config
from v_calculate_api_client import Configuration, ApiClient, ApiException

configuration = Configuration(
    host=f"http://{config['CALCULATE_API_HOST']}:{config['CALCULATE_API_PORT']}"
)


class VCalculateApiClient:

    def get_aggregates(self, name, since, to):
        with ApiClient(configuration) as api_client:
            api_instance = aggregate_api.AggregateApi(api_client)

            try:
                kwargs = dict(since=since, to=to)
                return api_instance.aggregate_name_get(name, **{k: v for k, v in kwargs.items() if v is not None})
            except ApiException as e:
                print('handle exception in calculate api client')
