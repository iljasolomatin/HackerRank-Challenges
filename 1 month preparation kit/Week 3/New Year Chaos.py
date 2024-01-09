#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    result=0
    for x in range(len(q)):
        if q[x] - x-1 >2:
            print( "Too chaotic")
            return
        else:
            ck =x
            while (ck!=0 and q[ck] < q[ck-1]) or ( ck >1 and q[ck] < q[ck-2]):
                temp = q[ck]
                q[ck] =q[ck-1]
                q[ck-1]=temp
                ck-=1
                result+=1
    print(result)        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
