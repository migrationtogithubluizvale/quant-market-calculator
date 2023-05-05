import unittest
from financial_interpolations.cubic_spline import CubicSplineInterpolator

class TestCubicSplineInterpolator(unittest.TestCase):
    def test_interpolate(self):
        interpolator = CubicSplineInterpolator()
        x_values = [1, 2, 3, 4, 5]
        y_values = [1, 4, 9, 16, 25]
        x = 2.5

        result = interpolator.interpolate(x_values, y_values, x)
        self.assertAlmostEqual(result, 6.5, places=6)

    def test_interpolate_invalid_length(self):
        interpolator = CubicSplineInterpolator()
        x_values = [1, 2, 3]
        y_values = [1, 4]

        with self.assertRaises(ValueError):
            interpolator.interpolate(x_values, y_values, 2.5)

    def test_interpolate_insufficient_data_points(self):
        interpolator = CubicSplineInterpolator()
        x_values = [1]
        y_values = [1]

        with self.assertRaises(ValueError):
            interpolator.interpolate(x_values, y_values, 2.5)
