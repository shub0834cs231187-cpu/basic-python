def sum_of_digits(n):
    # Base case: when number becomes 0
    if n == 0:
        return 0
    else:
        # Get last digit + sum of remaining digits
        return (n % 10) + sum_of_digits(n // 10)

# Taking input from user
num = int(input("Enter a number: "))

result = sum_of_digits(num)
print(f"Sum of digits of {num} is {result}")
