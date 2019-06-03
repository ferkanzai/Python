#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    fact = 1
    while n >= 1:
        fact *= n
        n -= 1
    return fact

if __name__ == '__main__':

    # NOTE: commented lines are only intended to work in HackerRank
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    result = factorial(n)

    #fptr.write(str(result) + '\n')
    #fptr.close()

    print(result)
