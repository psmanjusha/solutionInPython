# Python Program to read and print from csv.
# Read input from user. Use collections

import csv
with open('roll.csv',mode='r')as f:
  data = csv.reader(f)
  for row in data:
        print(row)
        
with open('roll.csv',mode='r')as f2:
  data2=csv.DictReader(f2)
  for raw in data2:
      print(raw['RollNo'])
