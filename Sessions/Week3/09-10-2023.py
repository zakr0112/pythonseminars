#imports
import time
import numpy as np

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
Five emams - five different marks
- Collect all marks in variables
"""


exam1 = int(input("Enter mark 1: "))

exam2 = int(input("Enter mark 2: "))

exam3 = int(input("Enter mark 3: "))

exam4 = int(input("Enter mark 4: "))

exam5 = int(input("Enter mark 5: "))

exams = [exam1, exam2, exam3, exam4, exam5]

print(exams)

highest = max(exams)
print("Highest:", highest)

lowest = min(exams)
print("Lowest: ", lowest)

print("Mean :", np.mean(exams))