def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

# Taking input from user
num = int(input("Enter a number: "))

# Calling the function and printing result
result = factorial(num)
print(f"Factorial of {num} is {result}")
