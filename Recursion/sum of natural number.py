def recursive_sum(n):
    # Base case: if n is 1, sum is 1
    if n == 1:
        return 1
    else:
        # Recursive case: n + sum of numbers till n-1
        return n + recursive_sum(n - 1)

# Taking input from user
num = int(input("Enter a number: "))

# Calling the function and printing result
result = recursive_sum(num)
print(f"Sum of first {num} natural numbers is {result}")
