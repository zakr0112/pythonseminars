#Imported
import time
time.gmtime(0)

#Global
pizzaNumber = 0
basePrice = 12
deliveryCost = 2.50
freeDelivery = 0


def BPP():
  time.sleep(1)
  print("Beckett Pizza Plaza")
  print("===================")
  time.sleep(1)
  startOrder()


def startOrder():
  try:
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
  deliveryReq = input("Is delivery required? (y/n): ")
  if deliveryReq == "y":
    if pizzaNumber >= 5:
      print("Delivery Cost:", freeDelivery)
    elif pizzaNumber < 5:
      print("Delivery Cost:", deliveryCost)
  elif deliveryReq == "n":
    print("Pickup Cost: 0")
  else:
    deliveryStart()

  print()
  print("===================")

  print()



#start
BPP()