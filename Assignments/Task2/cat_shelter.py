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
shortestVisit = 1440 #number of minutes in a day

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

    #Split the input string into 3 list sections
    splitList = item.split(",", 3)
    #print(splitList)
    iterator = iter(splitList)
    if next(iterator) == "OURS":
      myCatVisits = myCatVisits + 1
    else:
      otherCatVisits = otherCatVisits + 1
    startTime = int(next(iterator))
    endTime = int(next(iterator))
    #print(startTime)
    #print(endTime)
    # calculate visit time
    #visit time is end time - start time
    visitTime = endTime - startTime
    totalTime = totalTime + visitTime
    #shortestVisit = visitTime
    #print(visitTime)
    if visitTime > longestVisit:
      longestVisit = visitTime
    if visitTime <= shortestVisit:
      shortestVisit = visitTime
    
  
# We now need to split the string to work out the times

averageVisit = totalTime / totalVisits
totalHours, totalMins = divmod (totalTime, 60)



print()
print("Log File Analysis")
print("=================")
print()
print("Total Visits:", totalVisits)
print("Cat Visits:", myCatVisits)
print("Other Cats:", otherCatVisits)
print()
print("Total time in House:", totalHours, "Hours, ", totalMins, "Minutes")
print()
print("Average Visit:", round(averageVisit), "Minutes")
print("Longest Visit:", longestVisit, "Minutes")
print("Shortest Visit:", shortestVisit, "Minutes")
