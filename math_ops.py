# math_ops.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result or handles division by zero."""
    if b == 0:
        print("Cannot divide by 0")
        return None
    return a / b

def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

if __name__ == "__main__":
    x = 10
    y = 2
    result = divide_numbers(x, y)
    if result is not None:
        print(f"The result of division is: {result}")
        
    product = multiply_numbers(x, y)
    print(f"The result of multiplication is: {product}")
