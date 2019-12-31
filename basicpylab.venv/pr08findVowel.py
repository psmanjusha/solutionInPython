# Python Program to find whether the given letter is a vowel.
# Read input from user

a1 = input("Enter the letter")
a=str.upper(a1)
if a=='a' or a=='E' or a=='I' or a=='O' or a=='U':
    print(a1, " is a vowel")
else:
    print(a1, " is not a vowel")
