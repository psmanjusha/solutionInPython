# Python Program to sort elements in the list.
# Read input from user. Use collections

mylist=[]
for i in range(1,5):
    print("Enter the {} element".format(i))
    a=int(input())
    mylist.append(a)
mylist.sort()
print(mylist)
