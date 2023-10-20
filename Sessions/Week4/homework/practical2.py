# Practical 2 - Function String Test
"""
Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string
"""

def start():
  print()
  userInput = input("Enter some text: ")
  uppercase_count = 0
  lowercase_count = 0
  for letter in userInput:
    if letter.isupper():
      uppercase_count += 1
    elif letter.islower():
      lowercase_count += 1

  print("Uppercase:", uppercase_count)
  print("Lowercase: ", lowercase_count)



start()