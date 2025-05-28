import os
import time
import threading

cookies = 0


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


upgrade_store = {
    0: "+2 Cookies per click: $25",
    1: "Autoclicker (1 cookie per 2 seconds): $15",
    2: "Grandma (3 cookies per second): $50",
    3: "Super Autoclicker (10 cookies per second): $300",
}

actual_upgrades = {
    "click_power": 1.0,  # starts at +1 per click
    "autoclicks": 0.0,
}


def upgrade_shop():
    global cookies
    clear()
    print("===== UPGRADE STORE =====")
    for key in upgrade_store.keys():
        print(key)
    print("=========================")
    while True:
        choice = input("Choose an upgrade (or press Enter to exit): ").strip()
        if choice == "":
            break
        elif choice == "0" and cookies >= 25:
            clear()
            actual_upgrades["click_power"] += 2
            cookies -= 25
        elif choice == "1" and cookies >= 15:
            clear()
            actual_upgrades["autoclicks"] += 0.5
            cookies -= 15
        elif choice == "2" and cookies >= 50:
            clear()
            actual_upgrades["autoclicks"] += 3
            cookies -= 50
        elif choice == "3" and cookies >= 300:
            clear()
            actual_upgrades["autoclicks"] += 10
            cookies -= 300
        else:
            clear()
            print("Invalid choice")


def autogenerate():
    global cookies
    while True:
        time.sleep(1)
        cookies += actual_upgrades["autoclicks"]


def main():
    global cookies
    threading.Thread(target=autogenerate, daemon=True).start()
    while True:
        print("Python cookie clicker")
        print("Options:")
        print("1. Click cookie")
        print("2. Visit shop")
        print("3. View cookie data")
        print("4. Quit")
        choice = input("> ").strip()
        if choice == "1":
            clear()
            cookies += actual_upgrades["click_power"]
            print(f"+{actual_upgrades['click_power']} cookie(s)")
        elif choice == "2":
            upgrade_shop()
        elif choice == "3":
            clear()
            print(f"Cookies: {cookies}")
            print(f"Click power: {actual_upgrades['click_power']}/click")
            print(f"Clicks per second: {actual_upgrades['autoclicks']}/s")
        elif choice == "4":
            break
    print("bai")


if __name__ == "__main__":
    main()
