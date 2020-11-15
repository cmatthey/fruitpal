#  Coco Matthey
#  https://www.linkedin.com/in/coco-matthey/
from dataclasses import dataclass

@dataclass
class Cost:
    """
    Per code review, converted Cost to use dataclass
    """
    commodity: str
    pricePerTon: float
    tradeVolume: float
    variableOverhead: float
    fixedOverhead: float
    country: str

    @property
    def total(self) -> float:
        return round(self.tradeVolume * (self.pricePerTon + self.variableOverhead) + self.fixedOverhead, 2)

    def __str__(self):
        return "{} {:.2f} | ({:.2f}*{})+{:.0f}".format(self.country, self.total, self.pricePerTon + self.variableOverhead,
                                                       self.tradeVolume, self.fixedOverhead)
