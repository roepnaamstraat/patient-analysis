"""
This module counts the number of line in input
Input: a string
Output: total number of lines
"""

import sys

count = 0
for line in sys.stdin:
    count +=1

print(count, "lines in standard input")
