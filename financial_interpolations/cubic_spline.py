from scipy.interpolate import CubicSpline
from financial_interpolations._interpolator import Interpolator

class CubicSplineInterpolator(Interpolator):
    def __init__(self, allow_extrapolation: bool = False):
        super().__init__(allow_extrapolation)
    
    def interpolate(self, x_values, y_values, x):
        """
        Function that calculates cubic spline interpolation of financial values.

        Args:
            x_values (list): List of x values (e.g., business days).
            y_values (list): List of corresponding y values (e.g., financial values).
            x (float): The x value at which to interpolate.

        Returns:
            float: Interpolated financial value at the given x value.
        """

        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length.")

        if len(x_values) < 2:
            raise ValueError("At least two data points are required for interpolation.")

        # Calculate the cubic spline interpolation
        cs = CubicSpline(x_values, y_values)
        y_interpolated = cs(x)

        return y_interpolated
