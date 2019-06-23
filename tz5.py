#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
# my code    
    ss1 = list(set(s1))
    ss2 = list(set(s2))
    t = 0

    for i in range(len(ss1)):
        for j in range(len(ss2)):
            if ss1[i] == ss2[j]:
                t += 1
    if t > 0:
        return 'YES'
    else: 
        return 'NO'
# /my code
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()