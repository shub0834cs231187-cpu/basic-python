def gcd(a, b):
    # Base case
    if b == 0:
        return a
    else:
        # Recursive step
        return gcd(b, a % b)

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")

