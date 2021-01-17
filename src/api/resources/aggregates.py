from api.adapters.services.v_calculate_api_client import VCalculateApiClient
from api.business_logic.get_aggregates import GetAggregates


def get_aggregates(name: str, since: int = None, to: int = None):
    bl = GetAggregates(VCalculateApiClient())
    aggregates = bl.execute(name, since, to)
    return aggregates, 200
