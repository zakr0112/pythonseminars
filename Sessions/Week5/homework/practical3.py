#Practical 3 - sys module for command line arguments
"""
Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do
"""

import sys

number = len(sys.argv)
parsed = number - 1
print("Arguments passed", parsed)
print("")




