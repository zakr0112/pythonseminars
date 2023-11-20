#Practical 5 - Unix spell-checker (CLA Implementation)
"""
The Unix spell command is a simple spell-checker. It prints out all the words in a
text file that are not found in a dictionary. Write and test an implementation of this,
that takes a file name as a command-line argument.
Note: You may want to simplify the program at first by testing with a text file that
does not contain any punctuation. A complete version should obviously be able to
handle normal files, with punctuation
"""

print()

import sys
import string

fileName = sys.argv[1]

with open(sys.argv[1]) as fileName:
  for line in fileName:
     punctuationNotWords = ''.join(char for char in line if char in string.puncuation)
  