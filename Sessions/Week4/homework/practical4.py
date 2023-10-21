# Practical 4 - String Character Paramter
"""
When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)
"""

print()
def characterRemove():
  userInput = input("Enter a string: ")
  charRemoved = userInput[-1]
  print("Last character:", charRemoved)

characterRemove()