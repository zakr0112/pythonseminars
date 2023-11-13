#13/11/2023 - Practical Lab Session

#imports
import math
import time


#global variables
name = "Zak"
addr = "LS28AR"

def choiceone():
  #Format f Strings / Specifiers
  print("Format f Strings / Specifiers")
  print()
  name = input("Enter your name: ")
  addr = input("Enter your address: ")
  age = int(input("Enter you age: "))
  r = int(input("Enter a radius: "))
  print()
  print(f"Your name is {name}, and your address is {addr}")
  print(f"A circle with radius {r} has an area of {math.pi * r * r}")
  print(f"{name:15} - {age:10}")
  print(f"{name:0^15} - {age:#^10}")
  print()
  time.sleep(3)
  menu()



def choicetwo():
  #Formatting str.format()
  print("Formatting str.format()")
  name = input("Enter your name: ")
  age = int(input("Enter you age: "))
  item = input("Enter item name: ")
  cost = int(input("Enter it's price: "))
  print("Your name is {}, and you address is {}".format(name,addr))
  print("Your name is {1}, and your address is {0}".format(addr, name))
  print("Your name is {id}, and your address is {0}".format(addr, id = name))
  print("The cost of '{:^11}' was £{:8.2f}".format(item,cost))
  print(f"{name:@^15} - {age:#^10}")
  time.sleep(3)



def menu():
  print("(1): Format f Strings / Specifiers")
  print("(2): Formatting str.format()")
  choice = input("Enter your choice: ")
  if choice == "1":
    print()
    choiceone()
  elif choice == "2":
    print()
    choicetwo()


#start
menu()