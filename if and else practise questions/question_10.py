# Program to check whether a character is Uppercase or Lowercase

# Taking input from the user
ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print(ch, "is an Uppercase Alphabet.")
elif 'a' <= ch <= 'z':
    print(ch, "is a Lowercase Alphabet.")
else:
    print(ch, "is not an Alphabet.")
