import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets the person by name."""
    print(f"Hello, {name}!")

# Example usage
greet("Shubham")

# Check metadata
print("Function name:", greet.__name__)
print("Function docstring:", greet.__doc__)
