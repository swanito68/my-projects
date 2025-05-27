import math
import os


# Clear console
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Arithmetic
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


def subtract(initial, *nums):
    total = 0
    for num in nums:
        total += num
    initial -= total
    return initial
