import unittest

from legacy_code.src.ShippingCalculator import ShippingCalculator


class ShippingCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.shipping_calculator = ShippingCalculator()

    def test_should_calculate_standard_shipping(self):
        shipping_cost = self.shipping_calculator.calculate_shipping("1001")
        self.assertEqual(shipping_cost, 2.5)
    
    def test_should_calculate_express_shipping(self):
        shipping_cost = self.shipping_calculator.calculate_shipping("1002")
        self.assertEqual(shipping_cost, 36.8)

    def test_should_calculate_overnight_shipping(self):
        shipping_cost = self.shipping_calculator.calculate_shipping("1003")
        self.assertEqual(shipping_cost, 27.4)