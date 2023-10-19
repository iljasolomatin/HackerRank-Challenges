#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    if n == 1:
        return "Richard"
        
    currentTurn = "Louise"
    currentN = n
    
    while currentN != 1:
        binNum = str(bin(currentN))
        binNum = binNum[2:]
        oneCount = 0
        print("Turn start: ", currentN)
        
        # count number of 1s
        for bit in binNum:
            if bit == "1":
                oneCount += 1
                
        # if only one 1, then its a power of 2
        if oneCount == 1:
            currentN = int(currentN / 2)
            if currentTurn == "Louise":
                currentTurn = "Richard"
            else:
                currentTurn = "Louise"
        else:  # not a power of 2, so find the next lower power and reduce the current n
            lowerPower = "0b"
            for i in range(len(binNum)):
                if i == 0:
                    lowerPower += "1"
                else:
                    lowerPower += "0"
            currentN = currentN - int(lowerPower, 2)
            if currentTurn == "Louise":
                currentTurn = "Richard"
            else:
                currentTurn = "Louise"
        print("Turn end: ", currentN)
    
    if currentTurn == "Louise":
        return "Richard"
    else:
        return "Louise"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
