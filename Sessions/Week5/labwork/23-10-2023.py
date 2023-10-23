#Labwork - 23/10/2023 - Command Line Testing

#Prompts the user to enter a number
number = input("Enter a number: ")

#This stores the entered number
number = int(number)

#This outputs on the screen, the number that the user enters
print("The numbered entered was", number)

#This part does a calculation to work out if the number is even, or odd
if (number % 2) == 0:
  print("That is an even number")
else:
  print("That is an odd number")

if (number / 10):
  print("This number is divisible by 10")
else:
  print("This number is not divisible by 10")
