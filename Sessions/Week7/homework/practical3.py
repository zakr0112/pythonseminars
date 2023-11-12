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

print()


countries = ['England', 'Scotland', 'America', 'Italy', 'Germany']
capital_cities = ['London', 'Edinburgh', 'Washington DC', 'Rome', 'Berlin']

def capital(country):
  for i in range(len(countries)):
      if countries[i].lower() == country.lower():
          return capital_cities[i]
  return "Unknown"


def entry():


#run program
 entry()