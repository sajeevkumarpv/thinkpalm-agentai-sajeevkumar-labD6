
class Calculator:
    """A simple calculator class for performing basic calculations."""
    
    def calculate(self, operation, a, b):
        """
        Perform a calculation based on the operation specified.
        
        Args:
            operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
            a (float): The first number
            b (float): The second number
            
        Returns:
            float: The result of the calculation
            
        Raises:
            ValueError: If the operation is not supported
            ZeroDivisionError: If division by zero is attempted
        """
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError(f"Unsupported operation: {operation}")
    
    def add(self, a, b):
        """Add two numbers."""
        return self.calculate('add', a, b)
    
    def subtract(self, a, b):
        """Subtract two numbers."""
        return self.calculate('subtract', a, b)
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return self.calculate('multiply', a, b)
    
    def divide(self, a, b):
        """Divide two numbers."""
        return self.calculate('divide', a, b)
