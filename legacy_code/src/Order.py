from dataclasses import dataclass
import requests

@dataclass(frozen=True)
class Order:
    orderId: int
    shippingType: str
    weightKg: float
    distanceKm: float
    fragile: bool


class OrderService:

    def get_order(self, order_id: int) -> Order:
        url = f"https://codemanship.co.uk/api/orders.php?orderId={order_id}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        order = Order(
            orderId=data["orderId"],
            shippingType=data["shippingType"],
            weightKg=data["weightKg"],
            distanceKm=data["distanceKm"],
            fragile=data["fragile"]
        )
        return order