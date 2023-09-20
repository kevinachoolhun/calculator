"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from typing import Union

def add(a: Union[float, int], b: Union[float, int]):
    """Compute and return the sum of two numbers.
    
    Args:
        a(float): A number representing the first addend in the addition
        b(float): A number representing thee second addend in the addition. 
        
    Returns:
        float: A number representing the arithmetic sum of 'a' and 'b'.
    """
    return float(a + b)

def subtract(a, b):
    return float(a - b)

def multiply(a, b):
    return float(a * b)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)