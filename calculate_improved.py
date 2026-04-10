
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class EnhancedCalculator:
    """
    A calculator class that provides basic arithmetic operations with enhanced features.
    This class includes proper error handling, input validation, type hints, and logging.
    """

    def add(self, a: float, b: float) -> float:
        """Return the sum of two numbers."""
        self.validate_input(a, b)
        result = a + b
        logging.info(f'Adding {a} + {b} = {result}')
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of two numbers."""
        self.validate_input(a, b)
        result = a - b
        logging.info(f'Subtracting {a} - {b} = {result}')
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of two numbers."""
        self.validate_input(a, b)
        result = a * b
        logging.info(f'Multiplying {a} * {b} = {result}')
        return result

    def divide(self, a: float, b: float) -> float:
        """Return the quotient of two numbers."""
        self.validate_input(a, b)
        if b == 0:
            logging.error("Attempted to divide by zero.")
            raise ValueError("Cannot divide by zero.")
        result = a / b
        logging.info(f'Dividing {a} / {b} = {result}')
        return result

    def validate_input(self, *args: float) -> None:
        """Validate that all inputs are numbers."""
        for arg in args:
            if not isinstance(arg, (int, float)):
                logging.error(f'Invalid input: {arg}')
                raise TypeError(f'Invalid input: {arg}. Must be a number.')
