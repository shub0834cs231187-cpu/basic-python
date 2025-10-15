def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: fib(n) = fib(n-1) + fib(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Taking input from user
num = int(input("Enter the value of n: "))

result = fibonacci(num)
print(f"The {num}th Fibonacci number is {result}")
