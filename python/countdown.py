import time
from os import system


def countdown(seconds):
    for i in reversed(range(seconds + 1)):
        system("clear")
        print(i)
        time.sleep(1)
    print("Time's up!")


def main():
    a = 0
    userInput = None
    system("clear")
    running = True
    print("Welcome to my countdown program")
    while running:
        while a == 0:
            userInput = input("Enter a number of seconds (minimum: 1) :")
            if userInput.isdigit():
                userInput = int(userInput)
                if userInput < 1:
                    system("clear")
                    print("Input cannot be lower than 1")
                else:
                    a += 1
            else:
                system("clear")
                print("Invalid input")

        countdown(userInput)

        while True:
            match input("Use again? (Y/n): ").strip().lower():
                case "y":
                    system("clear")
                    print("Restarting")
                    a = 0
                    break
                case "n":
                    print("Quitting program")
                    running = False
                    break
                case _:
                    system("clear")
                    print("Invalid input")
    print("bai")


if __name__ == "__main__":
    main()
