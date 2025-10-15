def run_twice(func):
    def wrapper(*args, **kwargs):
        print("First execution:")
        func(*args, **kwargs)
        print("Second execution:")
        func(*args, **kwargs)
    return wrapper

@run_twice
def greet():
    print("Hello, Shubham!")

# Call the decorated function
greet()
