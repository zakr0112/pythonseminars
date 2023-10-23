import my_utils
from math import sqrt as root
import math as m
import math
import sys

#print("The square root of 20954 is", math.sqrt(20954))
#print("Average is", my_utils.average([10, 23, 30]))
#print("Another average is", my_utils.average([10.2, 8.8, 2.6]))

print()
print("The square root of 20954 is", root(20954))
print("The square root of 20954 is", m.sqrt(20954))
print("The sine 0.653 is", m.sin(0.653))
print("The cosine 0.623 is", m.cos(0.623))
print()

dir(math)
print()

print("The import search path for this program is", sys.path)