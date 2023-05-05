from abc import ABC, abstractmethod


class Interpolator(ABC):
    def __init__(self, allow_extrapolation: bool = False):
        """
        Initializes an instance of the Interpolator class.

        :param allow_extrapolation: A boolean indicating if extrapolation is allowed.
        """
        self.allow_extrapolation = allow_extrapolation

    @abstractmethod
    def interpolate(self, x_values, y_values, x):
        """
        Abstract method for interpolation. Must be implemented in subclasses.

        :param x_values: List of x values.
        :param y_values: List of y values.
        :param x: x value at which interpolation will be performed.
        :return: Interpolation result.
        """
        pass

    def extrapolate(self, x_values, y_values, x):
        """
        Method for extrapolation. Uses the interpolate method from subclasses.

        :param x_values: List of x values.
        :param y_values: List of y values.
        :param x: x value at which extrapolation will be performed.
        :return: Extrapolation result.
        :raises ValueError: If extrapolation is not allowed.
        """
        if not self.allow_extrapolation:
            raise ValueError("Extrapolation is not allowed for this instance of Interpolator")
        return self.interpolate(x_values, y_values, x)

    def can_extrapolate(self, x_values, x):
        """
        Checks if extrapolation is allowed and if the x value is outside the range of the provided x values.

        :param x_values: List of x values.
        :param x: x value to be checked.
        :return: True if extrapolation is possible, False otherwise.
        """
        return self.allow_extrapolation and (x < min(x_values) or x > max(x_values))
