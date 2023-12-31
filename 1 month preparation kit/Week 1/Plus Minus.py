#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for element in arr:
        if element > 0:
            pos += 1
        elif element < 0:
            neg += 1
        elif element == 0:
            zero += 1
    
    print(pos/n)
    print(neg/n)
    print(zero/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
