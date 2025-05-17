import os
from time import sleep
import random

symbols = ["7", "🍒", "🔔", "🍋", "🍉"]
money = random.randint(20, 500)


def shuffle():
    global money
    os.system("cls" if os.name == "nt" else "clear")
    result = [random.choice(symbols), random.choice(symbols), random.choice(symbols)]
    print("--- RESULT ---")
    sleep(3)
    print(f"| {result[0]} | {result[1]} | {result[2]} |")
    print("--------------")
    if result.count("7") == 3:
        print("Grand winner! You won 9999.99€!")
        money += 9999.99
    elif result.count("7") == 2:
        print("Winner! You won 2999.99€")
        money += 2999.99
    elif result.count("🍒") == 3:
        print("Winner! You won 999.99€")
        money += 999.99
    elif result.count("🍒") == 2:
        print("Winner! You won 250€")
        money += 250
    elif result.count("🔔") == 3:
        print("Winner! You won 129.99€")
        money += 129.99
    elif result.count("🔔") == 2:
        print("Winner! You won 59.99€")
        money += 59.99
    elif result.count("🍋") == 3:
        print("Winner! You won 39.99€")
        money += 39.99
    elif result.count("🍉") == 3:
        print("Winner! You won 19.99€")
        money += 19.99
    else:
        print("You lost! :(")


def main():
    global money
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to the casino")
    while True:
        print("Game price: 7.99€")
        choice = input("P to play, Q to quit, S to show balance: ").strip().lower()
        if money > 7.99:
            if choice == "p":
                money = money - 7.99
                shuffle()
            elif choice == "q":
                print("Goodbye")
                break
            elif choice == "s":
                print(f"Balance: {money:.2f}€")
            else:
                print("Invalid input")
        else:
            print("You do not have enough money!")


if __name__ == "__main__":
    main()
