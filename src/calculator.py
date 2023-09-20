
def add(a, b):
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