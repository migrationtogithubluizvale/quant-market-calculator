import unittest
from quant_market_calculator.interpolations.exponential import ExponentialInterpolator

class TestExponentialInterpolator(unittest.TestCase):
    def test_interpolate(self):
        interpolator = ExponentialInterpolator()
        y0 = 0.02
        y1 = 0.04
        WD0 = 0
        WD1 = 252
        WD = 126
        WD_prime = 252

        result = interpolator.interpolate(y0, y1, WD0, WD1, WD, WD_prime)
        self.assertAlmostEqual(result, 0.029998, places=6)

    def test_interpolate_same_day(self):
        interpolator = ExponentialInterpolator()
        y0 = 0.02
        y1 = 0.04
        WD0 = 0
        WD1 = 252
        WD = 0
        WD_prime = 252

        result = interpolator.interpolate(y0, y1, WD0, WD1, WD, WD_prime)
        self.assertAlmostEqual(result, y0, places=6)

    def test_interpolate_last_day(self):
        interpolator = ExponentialInterpolator()
        y0 = 0.02
        y1 = 0.04
        WD0 = 0
        WD1 = 252
        WD = 252
        WD_prime = 252

        result = interpolator.interpolate(y0, y1, WD0, WD1, WD, WD_prime)
        self.assertAlmostEqual(result, y1, places=6)
