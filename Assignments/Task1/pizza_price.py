#Imported
import time

time.gmtime(0)

#Global
basePrice = 12  #Sets the base price of the pizza outside of the functions


def BPP():
  time.sleep(1)
  print()
  print("=====================")
  print(" Beckett Pizza Plaza ")
  print("=====================")
  print()
  time.sleep(1)
  startOrder()


def startOrder():  #Starts the ordering process
  try:
    global pizzaNumber

    pizzaNumber = int(input("Pizza(s): "))
    if pizzaNumber == 0 or pizzaNumber < 1:
      print("> Oops! Please enter a higher number")
      print()
      time.sleep(1)
      startOrder()
  except ValueError:
    print("> Oops! Please enter a number")
    print()
    time.sleep(1)
    startOrder()
  print()
  print(">", pizzaNumber, "pizza(s) added to order")
  deliveryStart()


def deliveryStart():  #This calculates delivery cost based on input
  print()
  global deliveryReq  #Global variable for delivery request
  global deliveryCost  #Global variable for delivery cost
  deliveryCost = 2.50
  deliveryReq = input("Delivery (y/n): ")
  if deliveryReq == "y":
    if pizzaNumber >= 5:
      deliveryCost = deliveryCost - 2.50
      print()
      print("> Delivery Cost: £", round(deliveryCost, 2))
      print()
      tuesdayDiscount()
    elif pizzaNumber < 5:
      print()
      print("> Delivery Cost: £", round(deliveryCost, 2))
      print()
      tuesdayDiscount()
  elif deliveryReq == "n":
    print()
    print("> Delivery Cost: £0")
    print()
    deliveryCost = 0
    tuesdayDiscount()
  else:
    deliveryStart()


def tuesdayDiscount():  #Decides whether a discount will be applied
  global tuesdayOrNot
  tuesdayOrNot = input("Tuesday (y/n): ")
  if tuesdayOrNot == "y":
    print()
    print("> 50% Discount Applied")
    print()
  elif tuesdayOrNot == "n":
    print()
    print("> No Discount Available")
    print()
  else:
    tuesdayDiscount()
  bppAPP()


def bppAPP():  #BPP App discount
  global bppOrNot
  bppOrNot = input("BPP App (y/n): ")
  print()
  if bppOrNot == "y":
    print("> 25% Discount Applied")
  elif bppOrNot == "n":
    print()
    print("> No Discount Available")
    print()
  else:
    bppAPP()
  orderCalculation()


def orderCalculation():  #Starts the total calculation
  time.sleep(1)
  subtotal = basePrice * pizzaNumber + deliveryCost
  print()
  print()
  print("=====================")
  print("     BPP Receipt")
  print()
  print()
  print("Pizza(s):", pizzaNumber)
  print("Delivery Cost: £", deliveryCost)
  discount1 = 0
  discount2 = 0

  if tuesdayOrNot == "y":
    print()
    print("Tuesday Discount: 50%")
    discount1 = subtotal / 2
  elif tuesdayOrNot == "n":
    print("Tuesday Discount: 0%")
    discount1 = 0

  if bppOrNot == "y":
    print("BPP App Discount: 25%")
    discount2 = subtotal / 4
  elif bppOrNot == "n":
    print("BPP App Discount: 0%")
    discount2 = 0

  fulltotal = subtotal - discount1 - discount2  #Full receipt calculated
  print()
  print("Subtotal: £", round(subtotal, 2))
  print("Discount 1: £", round(discount1, 2))
  print("Discount 2: £", round(discount2, 2))
  print("Total: £", round(fulltotal, 2))
  print("=====================")
  print()
  print()
  print()
  time.sleep(5)
  orderAgain()


def orderAgain():  #Start another order or close program
  orderNew = input("Start another order? (y/n): ")
  if orderNew == "y":
    print()
    BPP()
  elif orderNew == "n":
    print()
    print("> Program Quit")
    time.sleep(1)
    quit()
  else:
    print()
    print("> Please type y/n")
    print()
    orderAgain()


#start
BPP()
