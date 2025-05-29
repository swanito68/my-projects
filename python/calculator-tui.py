# WORK IN PROGRESS!!!!!!!!!!!!!!!!!!!!!!!!!!
# planning to add geometry calc soon
import os
from typing import ValuesView


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
    for num in nums:
        initial -= num
    return initial


def multiply(*nums):
    product = 1
    for num in nums:
        product *= num
    return product


def divide(initial, *nums):
    for num in nums:
        if num == 0:
            raise ValueError("You can't divide by 0 you dumbo jumbo")
        initial /= num
    return initial


# Main program
def main():
    clear()
    print("Welcome to the arithmetic calculator I made")
    while True:
        print("1 -> Addition")
        print("2 -> Subtraction")
        print("3 -> Multiplication")
        print("4 -> Division")
        print("5 -> Exit")
        choice = input("==> ").strip()
        if choice == "5":
            break
        elif choice == "1":
            clear()
            print("Addition")
            while True:
                try:
                    count = int(input("Choose the amount of numbers (min: 2) "))
                    if count < 2:
                        print("Number of numbers must be above 2")
                        continue

                    numbers = []
                    for i in range(count):
                        while True:
                            try:
                                num = float(input(f"Number {i + 1} => "))
                                numbers.append(num)
                                break
                            except ValueError:
                                print("Input must be an int/float")

                    clear()
                    result = add(*numbers)
                    print(f"Result: {result:.2f}")
                    break
                except ValueError:
                    print("Input must be a number!!")
        elif choice == "2":
            clear()
            print("Subtraction")
            while True:
                try:
                    count = int(input("Choose the amount of numbers: (min. 2) "))
                    if count < 2:
                        print("Numbers must be above 2")
                        continue

                    numbers = []
                    for i in range(count):
                        while True:
                            try:
                                num = float(input(f"Number {i + 1} => "))
                                numbers.append(num)
                                break
                            except ValueError:
                                print("Input must be an int/float")

                    clear()
                    result = subtract(*numbers)
                    print(f"Result: {result:.2f}")
                except ValueError:
                    print("Input must be a number!!")
        elif choice == "3":
            clear()
            print("Multiplication")
            while True:
                try:
                    count = int(input("Choose the amount of numbers: (min. 2) "))
                    if count < 2:
                        print("Numbers must be above 2")
                        continue

                    numbers = []
                    for i in range(count):
                        while True:
                            try:
                                num = float(input(f"Number {i + 1} => "))
                                numbers.append(num)
                                break
                            except ValueError:
                                print("Input must be an int/float")

                    clear()
                    result = multiply(*numbers)
                    print(f"Result: {result:.2f}")
                except ValueError:
                    print("Input must be a number!!")
        elif choice == "4":
            clear()
            print("Division")
            while True:
                try:
                    count = int(input("Choose the amount of numbers: (min. 2) "))
                    if count < 2:
                        print("Numbers must be above 2")
                        continue

                    numbers = []
                    for i in range(count):
                        while True:
                            try:
                                num = float(input(f"Number {i + 1} => "))
                                numbers.append(num)
                                break
                            except ValueError:
                                print("Input must be an int/float")

                    clear()
                    try:
                        result = divide(*numbers)
                        print(f"Result: {result:.2f}")
                        break
                    except ValueError as ve:
                        print(f"Error: {ve}")
                        continue
                except ValueError:
                    print("Input must be a number!!")
        else:
            print("Invalid option")
            continue
    print("bai")


if __name__ == "__main__":
    main()
