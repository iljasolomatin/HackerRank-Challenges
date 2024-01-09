#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bombBlast(grid):
    x = len(grid)
    y = len(grid[0])
    blast = [['O'] * y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if grid[i][j] == 'O':
                blast[i][j] = '.'
                if i-1 >= 0:
                    blast[i-1][j] = '.'
                if j-1 >= 0:
                    blast[i][j-1] = '.'
                if i+1 < x:
                    blast[i+1][j] = '.'
                if j+1 < y:
                    blast[i][j+1] = '.'
    for i in range(len(blast)):
        blast[i] = ''.join(blast[i])
    return blast

def bomberMan(n, grid):
    # Write your code here'
    x = len(grid)
    y = len(grid[0])
    if n == 1:
        return grid
    if n % 2 == 0:
        return ['O' * y for _ in range(x)]
    
    blast = bombBlast(grid)
    blast2 = bombBlast(blast)
        
    if n % 4 == 1:
        return blast2
    if n % 4 == 3:
        return blast
                                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
