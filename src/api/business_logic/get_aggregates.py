from api.business_logic.models.aggregate import Aggregate


class GetAggregates:
    def __init__(self, api_client):
        self._api_client = api_client

    def execute(self, name: str, since: int, to: int) -> Aggregate:
        return Aggregate.create(self._api_client.get_aggregates(name, since, to))
