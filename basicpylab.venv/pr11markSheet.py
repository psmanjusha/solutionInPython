# Python Program to print marksheet.
# Read input from user. Use collections

subjectlist=[]
marklist=[]
for i in range(0,5):
    print("Enter subject {}".format(i))
    a=input()
    subjectlist.append(a)

for j in range(0,5):
    print("Enter the marks for {}".format(subjectlist[j]))
    b=int(input())
    marklist.append(b)

for k in range(0,5):
    print("The mark for {} = {}".format(subjectlist[k],marklist[k]))
print("The total mark = {}".format(sum(marklist)))
