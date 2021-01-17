from dataclasses import dataclass
from typing import List, Dict

from api.business_logic.models.common import BadRequestError
from api.business_logic.models.data import Data


@dataclass
class DataSeries:
    series: List[Data]

    @classmethod
    def create(cls, request: List[Dict]):
        try:
            return cls(
                series=[Data(entry['name'], entry['t'], entry['v']) for entry in request]
            )
        except Exception:
            raise BadRequestError(Exception)

    def to_point(self):
        return [data_entry.to_point() for data_entry in self.series]
