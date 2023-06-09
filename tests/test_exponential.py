import unittest
from financial_interpolations.exponential import ExponentialInterpolator

class TestExponentialInterpolator(unittest.TestCase):
    def test_interpolate(self):
        interpolator = ExponentialInterpolator()
        y0 = 0.02
        y1 = 0.03
        WD0 = 0
        WD1 = 252
        WD = 126
        WD_prime = 252
        result = interpolator.interpolate(y0, y1, WD0, WD1, WD, WD_prime)
        self.assertAlmostEqual(result, 0.014889156509221957, places=6)


    def test_interpolate_same_day(self):
        interpolator = ExponentialInterpolator()
        y0 = 0.02
        y1 = 0.04
        WD0 = 0
        WD1 = 252
        WD = 0
        WD_prime = 252

        result = interpolator.interpolate(y0, y1, WD0, WD1, WD, WD_prime)
        self.assertAlmostEqual(result, 0, places=6)

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
