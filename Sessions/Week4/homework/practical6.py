# Practical 6 - Centigrade temp into fahrenheit, and the reverse
"""
Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean
"""

print()
import time
import numpy as np
import statistics

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = 0
temp6 = 0

print("Temperature Program")
print("Enter 6 temperatures and it will work out:")
print("- Highest")
print("- Lowest")
print("- Mean")
print()

while temp1 == 0:
  temp1 = int(input("Enter temp 1: "))

while temp2 == 0:
  temp2 = int(input("Enter temp 2: "))

while temp3 == 0:
  temp3 = int(input("Enter temp 3: "))

while temp4 == 0:
  temp4 = int(input("Enter temp 4: "))

while temp5 == 0:
  temp5 = int(input("Enter temp 5: "))

while temp6 == 0:
  temp6 = int(input("Enter temp 6: "))

print()
temps = [temp1, temp2, temp3, temp4, temp5]

highest = max(temps)
print("Highest:", highest)

lowest = min(temps)
print("Lowest:", lowest)

print("Mean:", np.mean(temps))