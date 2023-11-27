#Imported
import time
time.gmtime(0)

#Global
pizzaNumber = 0
toppings = ""
base = 12


def BPP():
  time.sleep(1)
  print("Beckett Pizza Plaza")
  print("===================")
  time.sleep(1)
  startOrder()


def startOrder():
  try:
    pizzaNumber = int(input("Pizzas: "))
    if pizzaNumber > 5:
      print("Free delivery!")
    elif pizzaNumber < 5:
      print("Delivery fee will be charged")
  except ValueError:
    print("This is not a value!")
    time.sleep(1)
    startOrder()
  
  
  toppings = input("Toppings: ")
  tuesdayOrNot = input("Tuesday?: ")
  print()
  print("===================")

  print()



#start
BPP()