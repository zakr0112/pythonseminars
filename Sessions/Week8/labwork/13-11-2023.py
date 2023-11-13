#13/11/2023 - Practical Lab Session

#imports
import math
import time
import os


#global variables
name = "Zak"
addr = "LS28AR"
age = 18

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
  menu()


def choicethree():
  #Alternative Formatting Approaches
  print("Alternative Formatting Approaches")
  print("Name is %s, and age is %.2f" % (name, age))
  print(name.rjust(15), " - ", str(age).center(10))
  print(f"{name:>15} - {age:^10}")
  time.sleep(3)
  menu()


def choicefour():
  #File Handling
  print("File Handling")
  print()
  cwd = os.getcwd()
  files = os.listdir(cwd)
  print("Current Working Directory %r" % (cwd))
  print()
  print("FileHandle.txt Output: ")
  print()
  f = open("./Sessions/Week8/labwork/FileHandle.txt")
  file_contents = f.read()
  print(file_contents)
  for line in f:
    print(line)
  f.close()
  print()
  
  print()
  print("TextEdit.txt:")
  print("Current Contents: ")
  print()
  f1 = open("./Sessions/Week8/labwork/TextEdit.txt")
  file_contents = f1.read()
  
  print(file_contents)
  for line in f1:
    print(line)
  f1.close()
  print()
  f2 = open("./Sessions/Week8/labwork/TextEdit.txt", "w")
  writeToFile = input("Enter your text to write to file: ")
  f2.write(writeToFile)
  f2.close()
  print()
  print(writeToFile, "written to TextEdit.txt")


  time.sleep(3)
  menu()



def menu():
  print()
  print("(1): Format f Strings / Specifiers")
  print("(2): Formatting str.format()")
  print("(3): Alternative Formatting Approaches")
  print("(4): File Handling")
  choice = input("Enter your choice: ")
  if choice == "1":
    print()
    choiceone()
  elif choice == "2":
    print()
    choicetwo()
  elif choice == "3":
    print()
    choicethree()
  elif choice == "4":
    print()
    choicefour()
  else:
    print()
    print("Wrong Selection")
    menu()


#start
menu()