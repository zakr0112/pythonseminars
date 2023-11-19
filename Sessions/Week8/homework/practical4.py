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

fileName = sys.argv[2]


with open(sys.argv[1]) as fileName:
  linesCount = 0
  wordsCount = 0
  charactersCount = 0
  for line in fileName:
    linesCount += 1
    charactersCount += len(line)
    words = line.split()
    wordsCount += len(words)

print("Lines:", linesCount)
print("Words:", wordsCount)
print("Characters", charactersCount)