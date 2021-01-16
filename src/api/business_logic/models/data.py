from dataclasses import dataclass
from api.business_logic.models.common import BadRequestError


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

    def to_line(self):
        return f"{self.name} value={self.value} {self.time}"
