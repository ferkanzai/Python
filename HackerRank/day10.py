#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    lst = f"{n:b}".split('0')
    #print(f"{n:b}")
    #print(lst)
    longest = 0
    #the list comprehension doesn't work on all cases, as 439 (not always the longest strip is the first one)
    #longest = [i for i in lst if (len(i)) > 0]
    for i in lst:
        if len(i) > longest:
            longest = len(i)
    print(longest)
