import random
import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


dice_ascii = {
    1: (
        "┌-------┐",
        "|       |",
        "|   o   |",
        "|       |",
        "└-------┘",
    ),
    2: (
        "┌-------┐",
        "| o     |",
        "|       |",
        "|     o |",
        "└-------┘",
    ),
    3: (
        "┌-------┐",
        "| o     |",
        "|   o   |",
        "|     o |",
        "└-------┘",
    ),
    4: (
        "┌-------┐",
        "| o   o |",
        "|       |",
        "| o   o |",
        "└-------┘",
    ),
    5: (
        "┌-------┐",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "└-------┘",
    ),
    6: (
        "┌-------┐",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "└-------┘",
    ),
}


def show_dice(num_dices):
    rolls = [random.randint(1, 6) for _ in range(num_dices)]
    for i in range(0, num_dices, 3):
        batch = rolls[i : i + 3]
        for line in range(5):
            print("   ".join(dice_ascii[d][line] for d in batch))
        print()
    print(f"Total: {sum(rolls)}")


def main():
    clear()
    print("Dice roller program")
    while True:
        try:
            user_dice_num = int(input("Enter the number of dices: "))
            if user_dice_num <= 0:
                clear()
                print("Please enter a positive number.")
                return
            show_dice(user_dice_num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except KeyboardInterrupt:
            print()
            print("gudbai")
            exit()


if __name__ == "__main__":
    main()
