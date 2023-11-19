#Practical 4 - Unix wc command (CLA Implementation)
"""
The Unix wc command counts the number of lines, words, and characters in a file.
Write an implementation of this that takes a file name as a command-line
argument, and then prints the number of lines and characters.
Note: Linux (and Mac) users can use the "wc" command to check the results of their
implementation.
"""

print()

import sys

fileName = sys.argv[1]


with open(sys.argv[1]) as fileName:
  lines = 0
  words = 0
  characters = 0
  for lines in fileName:
    lines += 1
    characters += len(line)