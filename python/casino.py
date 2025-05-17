from os import system
from time import sleep
import random

symbols = ["7", "🍒", "🔔", "🍋", "🍉"]
money = random.randint(20, 500)


def shuffle():
    global money
    result = [random.choice(symbols), random.choice(symbols), random.choice(symbols)]
    print("--- RESULT ---")
    print(f"| {result[0]} | {result[1]} | {result[2]} |")
