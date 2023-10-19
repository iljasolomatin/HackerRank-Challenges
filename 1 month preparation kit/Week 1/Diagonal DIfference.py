#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    count = 0
    leftToRight = 0
    rightToLeft = 0
    
    for i, item in enumerate(arr):
        for j, element in enumerate(item):
            if i == j:
                leftToRight += element
                if i == len(arr) - 1 - i:
                    rightToLeft += element
            elif j == len(arr) - 1 - i:
                rightToLeft += element
    
    return abs(leftToRight - rightToLeft)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
