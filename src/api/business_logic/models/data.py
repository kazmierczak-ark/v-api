from dataclasses import dataclass
from api.business_logic.models.common import BadRequestError
from influxdb_client import Point, WritePrecision


@dataclass
class Data:
    name: str
    time: int
    value: float

    @classmethod
    def create(cls, name: str, time: int, value: float):
        try:
            return cls(
                name=name, time=time, value=value
            )
        except Exception:
            raise BadRequestError(Exception)

    def to_point(self):
        return Point(self.name).field("value", self.value).time(self.time, write_precision=WritePrecision.S)
