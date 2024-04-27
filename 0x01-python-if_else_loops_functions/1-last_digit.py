#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = abs(number) % 10
if (number < 0):
    last_dig = -last_dig
else:
    last_dig

if number > 5:
    print(f"Last digit of {number} is {last_dig} and is greater than 5")
elif number == 0:
    print("Last digit of {} is {} and is 0".format(number, last_dig))
elif (number < 6 & number != 0):
    print("Last digit of {number} is {last_dig} and is less than 6 and not 0")
