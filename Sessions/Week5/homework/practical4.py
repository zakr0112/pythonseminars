#Practical 4 - URL HTTP response codes
"""
Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
"""

import sys, getopt
import argparse


website = input("Enter website: ")