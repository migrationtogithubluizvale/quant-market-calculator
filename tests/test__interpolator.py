import unittest
from financial_interpolations._interpolator import Interpolator


class DummyInterpolator(Interpolator):
    def interpolate(self, x_values, y_values, x):
        return 0


class TestInterpolator(unittest.TestCase):
    def test_extrapolate(self):
        interpolator = DummyInterpolator(allow_extrapolation=True)
        x_values = [1, 2, 3]
        y_values = [1, 2, 3]
        x = 4

        result = interpolator.extrapolate(x_values, y_values, x)
        self.assertEqual(result, 0)

    def test_extrapolate_not_allowed(self):
        interpolator = DummyInterpolator(allow_extrapolation=False)
        x_values = [1, 2, 3]
        y_values = [1, 2, 3]
        x = 4

        with self.assertRaises(ValueError):
            interpolator.extrapolate(x_values, y_values, x)

    def test_can_extrapolate(self):
        interpolator = DummyInterpolator(allow_extrapolation=True)
        x_values = [1, 2, 3]

        self.assertTrue(interpolator.can_extrapolate(x_values, 4))
        self.assertFalse(interpolator.can_extrapolate(x_values, 2))

    def test_can_extrapolate_not_allowed(self):
        interpolator = DummyInterpolator(allow_extrapolation=False)
        x_values = [1, 2, 3]

        self.assertFalse(interpolator.can_extrapolate(x_values, 4))
        self.assertFalse(interpolator.can_extrapolate(x_values, 2))


