#!/usr/bin/python3
for alpha_letters in range(ord('a'), ord('z')+1):
    if alpha_letters in [ord('e'), ord('q')]:
        continue
    print("{:c}".format(alpha_letters), end="")
