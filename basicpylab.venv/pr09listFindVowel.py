# Python Program to find whether the given letter is a vowel.
# Read input from user. Use collections

a = input("Enter the letter")
b = str.lower(a)
mylist=['a','e','i','o','u']

if b in mylist:
    print(a, " is a vowel")
else:
    print(a, " is not a vowel")
