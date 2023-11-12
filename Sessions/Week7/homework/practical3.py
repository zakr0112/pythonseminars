#Practical 3 - Entry for capital cities
"""
Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on
"""

#Imports
import time


print()


countries = ['England', 'Scotland', 'America', 'Italy', 'Germany']
capital_cities = ['London', 'Edinburgh', 'Washington DC', 'Rome', 'Berlin']

def capital(country):
  for i in range(len(countries)):
      if countries[i].lower() == country.lower():
          return capital_cities[i]
  return "Unknown"


def entry():
  while True:
    countryentry = input("Enter a country (or type exit): ")
    if countryentry == "exit":
      quit()
    elif countryentry == {countries[0]}:
      print(f"The capital of {countryentry} is {capital_cities[0]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry == {countries[1]}:
      print(f"The capital of {countryentry} is {capital_cities[1]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry == {countries[2]}:
      print(f"The capital of {countryentry} is {capital_cities[2]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry == {countries[3]}:
      print(f"The capital of {countryentry} is {capital_cities[3]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry == {countries[4]}:
      print(f"The capital of {countryentry} is {capital_cities[4]}.")
      time.sleep(1)
      print()
      entry()


#run program
entry()