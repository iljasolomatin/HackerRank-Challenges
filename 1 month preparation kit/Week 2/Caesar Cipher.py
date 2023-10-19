#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    output = []
    
    for letter in s:
        # Capital letters
        if ord(letter) <= 90 and ord(letter) >= 65:
            encryptedChar = ord(letter) + k
            while encryptedChar > 90:
                encryptedChar -= 26
        # Lowercase letters
        elif ord(letter) <= 122 and ord(letter) >= 97:
            encryptedChar = ord(letter) + k
            while encryptedChar > 122:
                encryptedChar -= 26
        else:
            encryptedChar = ord(letter)
        
        encryptedChar = chr(encryptedChar)
        output.append(encryptedChar)
    output = "".join(output)
    return output
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
