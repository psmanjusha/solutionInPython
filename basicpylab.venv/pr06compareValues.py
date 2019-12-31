# Python Program to find greatest of two numbers. Read input from user
# Also check condition for equal

a = input("Enter the first number")
b = input("Enter the second number")
if a>b:
    print(a," is the greatest") 
elif b>a:
    print(b, " is the greatest")
else:
    print(a," ",b," Both are equal")
