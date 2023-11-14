#Practical 1 - Unix nl (CLA Implementation)
"""
The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for 
dry runs or white-box testing).

Write an implementation of this command. It should take the name of the
files as a command-line argument
"""

#Imports
import sys



filename = sys.argv[1]

with open(sys.argv[1]) as filename:
  for line in filename:
         print(line)

#Unsure how to do the line thing