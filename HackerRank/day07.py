#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    n = int(input())
    #list create a list, map returns a list as well of integers that are taken from input and splitted using " " and stripped of trailing " "
    arr = list(map(int, input().rstrip().split()))

    print(" ".join(map(str, arr[::-1])))
