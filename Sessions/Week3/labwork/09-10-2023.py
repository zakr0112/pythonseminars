#imports
import time
import numpy as np
import statistics

#Variable recap

order = 'eggs' + ' ' + 'spam'
order = 'eggs' + ' ' + 'spam' * 3

order = order[3:-1]
time.sleep(1)

knights = []
knights.append('Zak')

# task1
print("Task 1")
print(10 < 100)
print(100 != 100)
print(50 >= 50)
print()
"""
True
False
True

Works as intended
"""

# task2
print("Task 2")
print("a" < "b")
print("b" < "a")
print("John" < "Terry")
print()

#Marks Calculation

"""
Five exams - five different marks
- Collect all marks in variables
"""

exam1 = 101
exam2 = 101
exam3 = 101
exam4 = 101
exam5 = 101

while exam1 >100 and exam1:
  exam1 = int(input("Enter mark 1: "))

while exam2 >100:
  exam2 = int(input("Enter mark 2: "))

while exam3 >100:
  exam3 = int(input("Enter mark 3: "))

while exam4 >100:
  exam4 = int(input("Enter mark 4: "))

while exam5 >100:
  exam5 = int(input("Enter mark 5: "))

print()
exams = [ exam1, exam2, exam3, exam4, exam5]

print(exams)

highest = max(exams)
print("Highest:", highest)

lowest = min(exams)
print("Lowest: ", lowest)

print("Mean:", np.mean(exams))

print("Original :" + str(exams))
res = statistics.pstdev(exams)
print("Standard Deviation: " +str(res))