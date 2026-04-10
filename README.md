Name : SajeevKumar P V Track : Backend Dev Lab name :LabD3
Description:

# EnhancedCalculator Documentation

## Class: EnhancedCalculator

### Overview
The `EnhancedCalculator` class is an extension of basic calculator functionalities, incorporating advanced mathematical operations and features to enhance user experience.

### Features
- **Addition**: Adds two numbers and returns the result.
- **Subtraction**: Subtracts the second number from the first and returns the result.
- **Multiplication**: Multiplies two numbers and returns the result.
- **Division**: Divides the numerator by the denominator and returns the result, handling division by zero appropriately.
- **Power**: Raises a number to the power of another number.
- **Square Root**: Returns the square root of a number.

### Methods
1. **add(num1, num2)**: Returns the sum of `num1` and `num2`.
2. **subtract(num1, num2)**: Returns the difference of `num1` and `num2`.
3. **multiply(num1, num2)**: Returns the product of `num1` and `num2`.
4. **divide(num1, num2)**: Returns the quotient of `num1` divided by `num2`. Throws an error if `num2` is zero.
5. **power(base, exponent)**: Returns the result of raising `base` to the `exponent`.
6. **square_root(num)**: Returns the square root of `num`. Throws an error if `num` is negative.

### Example Usage
```python
calc = EnhancedCalculator()
print(calc.add(5, 3))  # Output: 8
print(calc.subtract(5, 3))  # Output: 2
print(calc.multiply(5, 3))  # Output: 15
print(calc.divide(5, 0))  # Output: Error: Cannot divide by zero
print(calc.power(2, 3))  # Output: 8
print(calc.square_root(16))  # Output: 4
