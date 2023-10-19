#!/bin/python3

import math
import os
import random
import re
import sys

def superDigit(n, k):
    
    if len(n) == 1:
        return int(n)
    
    summation = 0
    
    for i in range(len(n)):
        summation += int(n[i])
        
    return superDigit(str(summation * k), 1)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
