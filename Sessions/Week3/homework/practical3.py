# Practical 3 - Times Table Program

for i in range(0, 13):
  print(f"7 x {i} = {7 * i}")

userentry = int(input("Enter a number: "))
while userentry < 0 or userentry > 12:
  userentry = int(input("Enter a number: "))

calculation = userentry * 7
print(f"{userentry} x 7 = {calculation}")
while userentry < 12:
  userentry += 1
  calculation = userentry * 7
  print(f"{userentry} x 7 = {calculation}")
