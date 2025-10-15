import time

def delay_decorator(func):
    def wrapper(*args, **kwargs):
        print("Waiting for 1 second before executing...")
        time.sleep(1)  # delay for 1 second
        result = func(*args, **kwargs)
        return result
    return wrapper

@delay_decorator
def greet(name):
    print(f"Hello, {name}!")

# Example usage
greet("Shubham")
