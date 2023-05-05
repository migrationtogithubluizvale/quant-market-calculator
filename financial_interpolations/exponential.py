from financial_interpolations._interpolator import Interpolator


class ExponentialInterpolator(Interpolator):
    def __init__(self, allow_extrapolation: bool = False):
        super().__init__(allow_extrapolation)

    def interpolate(self, y0, y1, WD0, WD1, WD, WD_prime):
        """
        Function that calculates the exponential interpolation of interest rates.

        Args:
            y0 (float): Interest rate at the initial point (time 0).
            y1 (float): Interest rate at the final point (time 1).
            WD0 (int): Number of business days of the year up to time 0.
            WD1 (int): Number of business days of the year up to time 1.
            WD (int): Number of business days of the year up to the interpolation time.
            WD_prime (int): Total number of business days in the year.

        Returns:
            float: Interpolated interest rate at the interpolation time.
        """

        # Calculate the interpolated interest rate y'
        y_prime = (((1 + y0) ** (WD0 / 252)) * (((1 + y1) ** (WD1 / 252) / (1 + y0) ** (WD0 / 252)) ** ((WD - WD0) / (WD1 - WD0)))) ** (252 / WD_prime) - 1

        return y_prime
