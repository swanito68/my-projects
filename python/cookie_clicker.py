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
    4: "+10 Cookies per click: $100",
    5: "Cookie Factory (75 cookies per second): $2k",
    6: "+50 Cookies per click: $800",
    7: "+250 Cookies per click: $4k",
    8: "+33% Cookes per second: $250",
}

actual_upgrades = {
    "click_power": 1.0,  # starts at +1 per click
    "autoclicks": 0.0,
}


def upgrade_shop():
    global cookies
    clear()
    while True:
        print("============== UPGRADE STORE ==============")
        for key, value in upgrade_store.items():
            print(f"{key}: {value:10}")
        print("===========================================")
        print(f"You have {cookies} cookies")
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
        elif choice == "4" and cookies >= 100:
            clear()
            actual_upgrades["click_power"] += 10
            cookies -= 100
        elif choice == "5" and cookies >= 2000:
            clear()
            actual_upgrades["autoclicks"] += 75
            cookies -= 2000
        elif choice == "6" and cookies >= 800:
            clear()
            actual_upgrades["click_power"] += 50
            cookies -= 800
        elif choice == "7" and cookies >= 4000:
            clear()
            actual_upgrades["click_power"] += 250
            cookies -= 4000
        elif choice == "8" and cookies >= 250:
            clear()
            actual_upgrades["autoclicks"] *= 1.33
            cookies -= 250
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
        print(f"You have {cookies} cookies")
        print("Options:")
        print("Enter -> Click cookie")
        print("1     -> Visit shop")
        print("2     -> View cookie data")
        print("3     -> Quit")
        choice = input("> ").strip()
        if not bool(choice):
            clear()
            cookies += actual_upgrades["click_power"]
            print(f"+{actual_upgrades['click_power']} cookie(s)")
        elif choice == "1":
            upgrade_shop()
        elif choice == "2":
            clear()
            print(f"Click power: {actual_upgrades['click_power']}/click")
            print(f"Clicks per second: {actual_upgrades['autoclicks']}/s")
        elif choice == "3":
            break
        else:
            clear()
            print("Invalid input")
    print("bai")


if __name__ == "__main__":
    main()
