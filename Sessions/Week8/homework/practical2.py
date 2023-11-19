#Practical 2 - Unix diff command / Comparability of files (CLA Implementation)
"""
The Unix diff command compares two files and reports the differences, if any.
Write a simple implementation of this that takes two file names as command-line
arguments and reports whether or not the two files are the same. (Define "same" as
having the same contents.)
"""
print()

import sys



filename = sys.argv[1]
filename2 = sys.argv[2]

with open(sys.argv[1]) as filename:
  for line in filename:
         print(line)

with open(sys.argv[2]) as filename2:
  for line in filename2:
         print(line)

if filename == filename2:
  print("The file contents are the same")
else:
  print("The file contents are different")