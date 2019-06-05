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

    #print(arr)
    #print(len(arr))
    largest = []
    biggest = []

#this for loop creates an array with 4 arrays with the necesary numbers

    for i in range(4):
        line = []
        for x in range(4):
            line.append(arr[i][x:x+3])
            line.append(arr[i+1][x+1])
            line.append(arr[i+2][x:x+3])
        largest.append(line)
    #print(largest)

    for i in range(len(largest)):
        for x in range(0, len(largest[i]), 3):
            test = largest[i][x:x+3]
            #print(test)
            sum = 0
            for n in range(len(test)):
                if type(test[n]) == list:
                    for y in test[n]:
                        sum += y
                else:
                    sum += test[n]
            biggest.append(sum)
            #print(sum)
    #print(biggest)
    print(max(biggest))
