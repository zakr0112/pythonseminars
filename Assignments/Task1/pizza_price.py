#Imported
import time
time.gmtime(0)

#Global
basePrice = 12

def BPP():
  time.sleep(1)
  print("Beckett Pizza Plaza")
  print("===================")
  time.sleep(1)
  startOrder()


def startOrder():
  try:
    global pizzaNumber
    
    pizzaNumber = int(input("Pizzas: "))
    if pizzaNumber == 0 or pizzaNumber < 1:
      print("Oops! Please enter a higher number")
      print()
      time.sleep(1)
      BPP()
  except ValueError:
    print("Oops! Please enter a number")
    print()
    time.sleep(1)
    BPP()
  deliveryStart()


def deliveryStart():
  global deliveryReq
  global deliveryCost
  deliveryCost = 2.50
  deliveryReq = input("Is delivery required? (y/n): ")
  if deliveryReq == "y":
    if pizzaNumber >= 5:
      deliveryCost = deliveryCost - 2.50
      print("Delivery Cost:", deliveryCost)
      tuesdayDiscount()
    elif pizzaNumber < 5:
      print("Delivery Cost:", deliveryCost)
      tuesdayDiscount()
  elif deliveryReq == "n":
    print("Pickup Cost: 0")
    tuesdayDiscount()
  else:
    deliveryStart()


def tuesdayDiscount():
  global tuesdayOrNot
  tuesdayOrNot = input("Is it tuesday? (y/n): ")
  if tuesdayOrNot == "y":
    print("50% Discount Applied")
  elif tuesdayOrNot == "n":
    print("No Discount Available")
  else:
    tuesdayDiscount()
  bppAPP()


def bppAPP():
  global bppOrNot
  bppOrNot = input("Was the BPP app used? (y/n): ")
  if bppOrNot == "y":
    print("25% Discount Applied")
  elif bppOrNot == "n":
    print("No Discount Available")
  else:
    bppAPP()
  orderCalculation()


def orderCalculation():
  subtotal = basePrice * pizzaNumber + deliveryCost
  print()
  print("===================")
  print("Pizza's:", pizzaNumber)
  print("Delivery Cost:", deliveryCost)
    
  if tuesdayOrNot == "y":
    print("Tuesday Discount: 50% (y)")
    discount1 = subtotal / 2
  elif tuesdayOrNot == "n":
    print("Tuesday Discount: 0% (n)")
    discount1 = 0

  if bppOrNot == "y":
    print("BPP App Discount: 25% (y)")
    discount2 = subtotal / 4
  elif bppOrNot == "n":
    print("BPP App Discount: 0% (y)")
    discount2 = 0

  fulltotal = subtotal - discount1 - discount2
  print()
  print("Subtotal:", subtotal)
  print("Discount 1:", discount1)
  print("Discount 2:", discount2)
  print("Total:", fulltotal)
  print()

#start
BPP()