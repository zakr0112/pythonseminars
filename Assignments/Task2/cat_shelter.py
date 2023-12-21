import sys

if len(sys.argv) < 2:
    print("Missing command line argument")
    quit()


filename = sys.argv[1]
acceptedFiles = ['cat_shelter_1.txt', 'cat_shelter_2.txt', 'cat_shelter_3.txt']
if filename not in acceptedFiles:
    print("Cannot open that file")
    quit()


#Defining Variables for output
myCatVisits = 0
otherCatVisits = 0
totalVisits = 0
totalTime = 0
averageVisit = 0
longestVisit = 0
shortestVisit = 0

"""
print("Log File:", filename);print()  
fileObject = open(filename, 'r')
fileRead = fileObject.readline()
print(fileRead)
"""

with open(filename) as file:
  for item in file:
    if item.startswith("END"):
      break
    totalVisits = totalVisits + 1
    if item.startswith("OURS"):
      myCatVisits = myCatVisits + 1
    if item.startswith("THEIRS"):
      otherCatVisits = otherCatVisits + 1
    print(item)

print()
print("Log File Analysis")
print("=================")
print("Total Visits:", totalVisits)
print("Our Cat Visits:", myCatVisits)
print("Other Cat Visits:", otherCatVisits)
