from financial_interpolations._interpolator import Interpolator

class LinearInterpolator(Interpolator):
    def interpolate(y0, y1, WD0, WD1, WD):
        """
        Function that calculates linear interpolation of financial values.

        Args:
            y0 (float): Financial value at the initial point (time 0).
            y1 (float): Financial value at the final point (time 1).
            WD0 (int): Number of business days of the year up to time 0.
            WD1 (int): Number of business days of the year up to time 1.
            WD (int): Number of business days of the year up to the interpolation time.

        Returns:
            float: Interpolated financial value at the interpolation time.
        """

        if WD0 == WD1:
            raise ValueError("The WD values cannot be the same.")

        # Calculate the interpolated financial value y'
        y_prime = y0 + ((y1 - y0) * (WD - WD0)) / (WD1 - WD0)

        return y_prime

        