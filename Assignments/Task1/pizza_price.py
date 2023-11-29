#Imported
import time

time.gmtime(0)

#Global
basePrice = 12


def BPP():
  time.sleep(1)
  print()
  print("=====================")
  print(" Beckett Pizza Plaza ")
  print("=====================")
  print()
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
      startOrder()
  except ValueError:
    print("Oops! Please enter a number")
    print()
    time.sleep(1)
    startOrder()
  deliveryStart()


def deliveryStart():
  global deliveryReq
  global deliveryCost
  deliveryCost = 2.50
  deliveryReq = input("Delivery (y/n): ")
  if deliveryReq == "y":
    if pizzaNumber >= 5:
      deliveryCost = deliveryCost - 2.50
      print("Delivery Cost: £", round(deliveryCost, 2))
      tuesdayDiscount()
    elif pizzaNumber < 5:
      print("Delivery Cost: £", round(deliveryCost, 2))
      tuesdayDiscount()
  elif deliveryReq == "n":
    print("Delivery Cost: £0")
    deliveryCost = 0
    tuesdayDiscount()
  else:
    deliveryStart()


def tuesdayDiscount():
  global tuesdayOrNot
  tuesdayOrNot = input("Tuesday (y/n): ")
  if tuesdayOrNot == "y":
    print("50% Discount Applied")
  elif tuesdayOrNot == "n":
    print("No Discount Available")
  else:
    tuesdayDiscount()
  bppAPP()


def bppAPP():
  global bppOrNot
  bppOrNot = input("BPP App (y/n): ")
  if bppOrNot == "y":
    print("25% Discount Applied")
  elif bppOrNot == "n":
    print("No Discount Available")
  else:
    bppAPP()
  orderCalculation()


def orderCalculation():
  time.sleep(1)
  subtotal = basePrice * pizzaNumber + deliveryCost
  print()
  print()
  print("=====================")
  print("     BPP Receipt")
  print()
  print()
  print("Pizza's:", pizzaNumber)
  print("Delivery Cost: £", deliveryCost)
  discount1 = 0
  discount2 = 0

  if tuesdayOrNot == "y":
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

  fulltotal = subtotal - discount1 - discount2
  print()
  print("Subtotal: £", round(subtotal, 2))
  print("Discount 1: £", round(discount1, 2))
  print("Discount 2: £", round(discount2, 2))
  print("Total: £", round(fulltotal, 2))
  print("=====================")
  print()
  quit()


#start
BPP()
