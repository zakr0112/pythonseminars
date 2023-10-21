# Practical 5 - Convert Temparatures
"""
Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).
"""

import time

print()
print("Conversion Program")
print()

def choice():
  print("1. Centigrade to Fahrenheit")
  print("2. Fahrenheit to Centigrade")
  choices = input("Choice: ")
  if choices == "1":
    print()
    centToFah()
  elif choices == "2":
    print()
    fahToCent()
  else:
    print()
    choice()
    print()

def centToFah():
  print()
  print("(1) Centigrade to Fahrenheit:")
  celcius = int(input("Enter temperature: "))
  print()
  fahrenheit = (1.8* celcius) + 32
  print("Centigrade:", celcius)
  print("Fahrenheit:", fahrenheit)
  time.sleep(5)
  choice()
  print()


def fahToCent():
  print()
  print("(2) Fahrenheit to Centigrade:")
  fahrenheit = int(input("Enter temperature: "))
  print()
  celcius = (fahrenheit - 32)*5/9
  print("Fahrenheit:", fahrenheit)
  print("Centigrade:", celcius)
  time.sleep(5)
  choice()



choice()