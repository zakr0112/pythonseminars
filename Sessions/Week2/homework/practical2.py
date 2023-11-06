#Practical 2 - Celcius to fahrenheit (input)
"""
Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit
"""

print()

temperature = int(input("Enter Temperature: "))
fahrenheit = 1.8* temperature + 32

print("Celcius:", temperature)
print("Fahrenheit:", fahrenheit)