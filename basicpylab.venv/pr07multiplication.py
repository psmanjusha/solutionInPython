# Python Program to find the multiplication table of given number.
# Read input from user

a = int(input("Enter the number"))
i=1
while(i<11):
    print(i," ","X"," ",a," ","="," ",a*i)
    i=i+1
