#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    hour = None
    AMPM = None
    timeBody = None
    convertedTime = None
    
    hour = s[:2]
    AMPM = s[-2:]
    timeBody = s[2:-2]
    
    if AMPM == "AM":
        convertedTime = "" + (hour)
        if convertedTime == "12":
            convertedTime = "00"
        convertedTime += (timeBody)
    elif AMPM == "PM":
        convertedTime = "" + str(int(hour) + 12)
        if convertedTime == "24":
            convertedTime = "12"
        convertedTime += (timeBody)
    
    return(convertedTime)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
