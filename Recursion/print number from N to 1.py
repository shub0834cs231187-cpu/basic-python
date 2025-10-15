def print_reverse(n):
    # Base case
    if n == 0:
        return
    # Print first for decreasing order
    print(n, end=" ")
    # Recursive call for smaller number
    print_reverse(n - 1)

# Taking input from user
num = int(input("Enter a number: "))

print(f"Numbers from {num} to 1:")
print_reverse(num)
