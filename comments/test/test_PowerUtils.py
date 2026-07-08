import unittest

from comments.src.PowerUtils import PowerUtils


class TestPowerUtils(unittest.TestCase):

    def test_n_basic(self):
        self.assertEqual(PowerUtils.n(0), 0)
        self.assertEqual(PowerUtils.n(2), 4)
        self.assertEqual(PowerUtils.n(-3), 9)

    def test_m_single_value(self):
        self.assertEqual(PowerUtils.m(3, 3), 9)

    def test_m_small_range(self):
        self.assertEqual(PowerUtils.m(1, 3), 14)

    def test_m_larger_range(self):
        self.assertEqual(PowerUtils.m(0, 3), 14)

    def test_m_negative_range(self):
        self.assertEqual(PowerUtils.m(-2, 0), 5)

    def test_m_larger_negative_to_positive(self):
        self.assertEqual(PowerUtils.m(-1, 1), 2)


if __name__ == "__main__":
    unittest.main()
