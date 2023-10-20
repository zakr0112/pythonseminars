# Practical 1 - Function Test
"""
Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise
"""

def ValidInput():
  print()
  validNum = int(input("Enter integar between 0 and 100: "))
  if validNum < 0 or validNum > 100:
        print("False")
  else:
        print("True")
    

ValidInput()
