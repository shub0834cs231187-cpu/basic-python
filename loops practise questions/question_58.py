# Python program to print star pattern using nested for loop

# number of rows for the upper half
n = 10

# upper half of the pattern
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()   # move to next line

# lower half of the pattern
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
