def my_decorator(func):
    def wrapper():
        print("Starting function")
        print("Ending function")
        func()
        
    return wrapper

@my_decorator
def say_hello():
    print("Hello, Shubham!")

# Call the decorated function
say_hello()
