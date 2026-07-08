from dataclasses import dataclass
import requests

@dataclass(frozen=True)
class Order:
    orderId: int
    shippingType: str
    weightKg: float
    distanceKm: float
    fragile: bool


class Order:
    pass