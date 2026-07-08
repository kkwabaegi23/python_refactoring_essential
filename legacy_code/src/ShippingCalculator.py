from legacy_code.src.Order import Order


class ShippingCalculator:

    def calculate_shipping(self, order_id: int) -> float:
        try:
            order = self.fetch_order(order_id)

            if order.shippingType == "STANDARD":
                return order.weightKg * 0.5

            elif order.shippingType == "EXPRESS":
                return order.weightKg * 0.8 + order.distanceKm * 0.1

            elif order.shippingType == "OVERNIGHT":
                return order.weightKg * 1.2 + 25

            else:
                raise RuntimeError(f"Unknown shipping type: {order.shippingType}")

        except Exception as e:
            print(e)
            return -1.0

    def fetch_order(order_id: int) -> Order:
        
        order = Order().get_order(order_id)
        return order