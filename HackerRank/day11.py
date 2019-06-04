#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    print(len(arr))
    largest = 0
    one = None
    two = None
    three = None

    for i in range(4):
        one = [arr[i][i:i+3]]#, arr[i+1][i:i+3]]#, arr[i+2][i:i+3]]
        print(one)
    print(two)
    print(three)
