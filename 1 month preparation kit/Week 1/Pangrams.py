#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    seenValues = []
    
    for letter in s:
        if letter.lower() not in seenValues and letter != " ":
            seenValues.append(letter.lower())
    
    return "pangram" if len(seenValues) == 26 else "not pangram"
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
