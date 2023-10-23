#Practical 1 - sys module to detect OS
"""
Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used.
"""

import sys
import platform

print()
print("OS", sys.platform)
print("Architecture", platform.architecture())
print("Hostname", platform.node())