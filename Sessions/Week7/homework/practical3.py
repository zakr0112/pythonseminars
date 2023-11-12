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
    print()
    print("Current Known Countries:", countries)
    print();print()
    countryentry = input("Enter a country (or type exit): ")
    if countryentry == "exit":
      quit()
    elif countryentry == "England":
      print(f"The capital of {countryentry} is {capital_cities[0]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry == "Scotland":
      print(f"The capital of {countryentry} is {capital_cities[1]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry == "America":
      print(f"The capital of {countryentry} is {capital_cities[2]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry == "Italy":
      print(f"The capital of {countryentry} is {capital_cities[3]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry == "Germany":
      print(f"The capital of {countryentry} is {capital_cities[4]}.")
      time.sleep(1)
      print()
      entry()
    elif countryentry is not countries:
      print("Whoops that's not in our list!")
      newcountry = input("Re-enter the city: ")
      newcity = input("Enter its capital city: ")
      countries.append(newcountry)
      capital_cities.append(newcity)
      time.sleep(1)
      print()
      entry()


#run program
entry()