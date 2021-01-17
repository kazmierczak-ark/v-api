from dataclasses import dataclass


@dataclass
class Aggregate:
    avg: float
    sum: float

    @classmethod
    def create(cls, values_dict):
        return cls(
            avg=values_dict['avg'], sum=values_dict['sum']
        )
