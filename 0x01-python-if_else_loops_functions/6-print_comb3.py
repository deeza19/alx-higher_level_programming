#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{:0d}{:0d}".format(i, j), end="\n")
        else:
            print("{:0d}{:0d}".format(i, j), end=",")
