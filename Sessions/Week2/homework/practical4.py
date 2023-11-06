#Practical 4 - Division between input
"""
A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over.

"""

print()

tubofsweets = int(input("Enter how many sweets there are: "))
pupils = int(input("How many attended: "))

print()
calculation = tubofsweets / pupils
print(calculation)