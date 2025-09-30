# Program to reverse a 4-digit number

# Input 4-digit number
num = int(input("Enter a 4-digit number: "))

# Check if number is 4-digit
if 1000 <= num <= 9999:
    # Reversing the number
    reversed_num = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp = temp // 10
    
    print(f"Reversed Number: {reversed_num}")
else:
    print("ERROR: Please enter a 4-digit number.")
