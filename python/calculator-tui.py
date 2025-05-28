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


def multiply(*nums):
    product = 0
    for num in nums:
        product *= num
    return product


def R_divide(initial, *nums):
    total = sum(nums)
    if total == 0:
        raise ValueError("Cannot divide by 0")
    return initial / total


def S_divide(initial, *nums):
    for num in nums:
        initial /= num
    return initial
