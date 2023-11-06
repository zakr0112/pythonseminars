#Practical 3 - Prime Number Parameter Function
"""
Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.
"""

print()

IntIntegar = int(input("Enter Integar: "))

if IntIntegar > 1:
  for i in range(2, int(IntIntegar/2)+1):
    if (IntIntegar % i) == 0:
      print(IntIntegar, "is not prime")
      break
  else:
    print(IntIntegar, "is prime")

else:
    print(IntIntegar, "is not prime")
