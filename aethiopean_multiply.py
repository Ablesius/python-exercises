#!/usr/bin/env python3

import sys

firstFactor = int(sys.argv[1])
secondFactor = int(sys.argv[2])
firstArray = []
secondArray = []

firstArray.append(firstFactor)
secondArray.append(secondFactor)

while firstArray[-1] is not 1:
    firstArray.append(int(firstArray[-1]/2))

while len(secondArray) is not len(firstArray):
    secondArray.append(secondArray[-1]*2)

rightIndices = []
for f in firstArray:
    # left factor is odd
    if f/2 != int(f/2):
       rightIndices.append(firstArray.index(f))

rightNumbers = []
for index in rightIndices:
    rightNumbers.append(secondArray[index])


if sum(rightNumbers) != firstFactor * secondFactor:
    print("Something went wrong")
else:
    print(sum(rightNumbers))
