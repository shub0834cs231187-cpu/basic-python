# Program to count number of digits in a number

# Taking input from user
num = int(input("Enter a number: "))

count = 0
n = num

# Loop until number becomes 0
while n > 0:
    n //= 10
    count += 1

print("Number of digits in", num, "is:", count)
