#Practical 4 - Encryption Function
"""
Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.
"""

print()

message = input("Enter your string: ")

def remove_space(message):
  return message.replace(" ", "")

print("Part 1:", remove_space(message))