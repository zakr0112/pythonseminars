import sys

if len(sys.argv) < 2:
    print("Missing command line argument")
    quit()

filename = sys.argv[1]
acceptedFiles = ['cat_shelter_1.txt', 'cat_shelter_2.txt', 'cat_shelter_3.txt']
"""
if filename not in acceptedFiles:
    print("Cannot open that file")
    quit()

"""
#Defining Variables for output
myCatVisits = 0
otherCatVisits = 0
totalTime = 0
averageVisit = 0
longestVisit = 0
shortestVisit = 0


print("Log File:", filename);print()  
fileObject = open(filename, 'r')
fileRead = fileObject.readline()
print(fileRead)

print("Log File Analysis")

