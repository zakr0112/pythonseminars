#Practical 4 - URL HTTP response codes
"""
Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
"""

import sys 
import getopt
import requests
import argparse
from http import HTTPStatus

print()
url = str(sys.argv[1])
response = requests.get(url)
print("Response Code:", response.status_code)