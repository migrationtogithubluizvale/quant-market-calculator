from abc import ABC, abstractmethod

class Capture(ABC):
    """
    This is an abstract base class for capturing data. It provides a common interface
    for concrete classes to implement. The interface consists of two abstract methods,
    run() and resolve().
    """

    @abstractmethod
    def run(self, date):
        """
        This abstract method should be implemented by the concrete class to perform
        the data capturing process. It receives a date parameter, which will be used
        by the concrete implementation.

        Args:
            date: The date for which data should be captured.
        """
        self.date = date

    @abstractmethod
    def resolve(self):
        """
        This abstract method should be implemented by the concrete class to process
        the captured data. It checks if the date is defined before proceeding.
        
        Raises:
            Exception: If the date is not defined.
        """
        if self.date is None:
            raise Exception("Date is not defined")
