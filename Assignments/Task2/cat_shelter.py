import sys
import os

if len(sys.argv) < 2:
    print("Missing command line argument")
    quit()

filename = sys.argv[1]
acceptedFiles = ['cat_shelter_1.txt', 'cat_shelter_2.txt', 'cat_shelter_3.txt']

if filename not in acceptedFiles:
    print("Cannot open that file")
    quit()
else:
    print("Log File:", filename);print()  
    open(filename, 'r')

print("Log File Analysis")

