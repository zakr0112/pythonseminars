#Practical 2 - sys module to report arguments
"""
Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument).
"""

import sys

number = len(sys.argv)
parsed = number - 1
print("Arguments passed", parsed)