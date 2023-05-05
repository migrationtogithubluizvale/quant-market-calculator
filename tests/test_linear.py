import unittest
from financial_interpolations.linear import LinearInterpolator

class TestLinearInterpolator(unittest.TestCase):
    def test_interpolate(self):
        interpolator = LinearInterpolator()
        y0 = 1
        y1 = 2
        WD0 = 0
        WD1 = 252
        WD = 126

        result = interpolator.interpolate(y0, y1, WD0, WD1, WD)
        self.assertAlmostEqual(result, 1.5, places=6)

    def test_interpolate_same_day(self):
        interpolator = LinearInterpolator()
        y0 = 1
        y1 = 2
        WD0 = 0
        WD1 = 252
        WD = 0

        result = interpolator.interpolate(y0, y1, WD0, WD1, WD)
        self.assertAlmostEqual(result, y0, places=6)

    def test_interpolate_last_day(self):
        interpolator = LinearInterpolator()
        y0 = 1
        y1 = 2
        WD0 = 0
        WD1 = 252
        WD = 252

        result = interpolator.interpolate(y0, y1, WD0, WD1, WD)
        self.assertAlmostEqual(result, y1, places=6)

    def test_interpolate_same_WD_values(self):
        interpolator = LinearInterpolator()
        y0 = 1
        y1 = 2
        WD0 = 0
        WD1 = 0
        WD = 0

        with self.assertRaises(ValueError):
            interpolator.interpolate(y0, y1, WD0, WD1, WD)
