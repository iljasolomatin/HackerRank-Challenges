#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    uniqueAr = []
    numPairs = 0
    
    for item in ar:
        if item not in uniqueAr:
            uniqueAr.append(item)
    
    for item in uniqueAr:
        pairs = ar.count(item)
        pairs = int(pairs / 2)
        
        numPairs += pairs
        
    return numPairs
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
