import multiprocessing as mp
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
        #overkill that slows down processing for small amounts of data - normally would base choice on exact business cases expected
        pool = mp.Pool(mp.cpu_count())
        points = pool.map(DataSeries.data_entry_to_point, self.series)
        pool.close()
        pool.join()
        return points

    @staticmethod
    def data_entry_to_point(data: Data):
        return data.to_point()
