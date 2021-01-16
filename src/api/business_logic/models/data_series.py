from dataclasses import dataclass
from typing import List, Dict

from api.business_logic.models.data import Data
from api.business_logic.models.common import BadRequestError


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

    def to_line(self):
        return [data_entry.to_line() for data_entry in self.series]