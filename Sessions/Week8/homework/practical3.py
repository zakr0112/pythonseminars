#Practical 3 - Unix grep command (CLA Implementation)
"""
The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string.
"""
import sys

print()

grepFileName = sys.argv[1]
stringInFile = sys.argv[2]

with open(sys.argv[1]) as grepFileName:
  lines = grepFileName.readlines()
  matchingString = [line.strip() for line in lines if stringInFile in line]
  if matchingString:
    for line in matchingString:
      print("Lines including: ", stringInFile)
      print(line)
  


