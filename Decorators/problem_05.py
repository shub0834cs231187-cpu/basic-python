def uppercase_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

# Example usage
@uppercase_output
def greet(name):
    return f"Hello {name}"

@uppercase_output
def add(a, b):
    return a + b  # This will not be affected, since it's not a string

print(greet("Shubham"))  # Output: HELLO SHUBHAM
print(add(5, 3))         # Output: 8
