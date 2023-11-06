#Practical 2 - Factors Parameter Function
"""
Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to yield the original).
"""

print()

Integar = int(input("Enter Integar: "))
for i in range(1,Integar+1):
  if not Integar%i:
    print(i,end=' ')