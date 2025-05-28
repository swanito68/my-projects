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
    8: "+33% Cookies per second: $250",
    9: "+33% Cookies per click: $500",
    10: "Cookie Bank (+400 Cookies per click): $6k",
    11: "x2 Cookies per second: $3.5k",
}

actual_upgrades = {"click_power": 1.0, "autoclicks": 0.0}


def upgrade_shop():
    global cookies
    clear()
    while True:
        print("================== UPGRADE STORE ==================")
        for key, value in upgrade_store.items():
            print(f"{key} -> {value}")
            if len(str(key)) > 1:
                print(f"{key}  -> {value}")
        print("===================================================")
        print(f"You have {cookies:.2f} cookies")
        choice = input("Choose an upgrade (or press Enter to exit): ").strip()
        if choice == "":
            break
        elif choice == "0" and cookies >= 25:
            clear()
            actual_upgrades["click_power"] += 2
            cookies -= 25
            print("Successfully bought")
        elif choice == "1" and cookies >= 15:
            clear()
            actual_upgrades["autoclicks"] += 0.5
            cookies -= 15
            print("Successfully bought")
        elif choice == "2" and cookies >= 50:
            clear()
            actual_upgrades["autoclicks"] += 3
            cookies -= 50
            print("Successfully bought")
        elif choice == "3" and cookies >= 300:
            clear()
            actual_upgrades["autoclicks"] += 10
            cookies -= 300
            print("Successfully bought")
        elif choice == "4" and cookies >= 100:
            clear()
            actual_upgrades["click_power"] += 10
            cookies -= 100
            print("Successfully bought")
        elif choice == "5" and cookies >= 2000:
            clear()
            actual_upgrades["autoclicks"] += 75
            cookies -= 2000
            print("Successfully bought")
        elif choice == "6" and cookies >= 800:
            clear()
            actual_upgrades["click_power"] += 50
            cookies -= 800
            print("Successfully bought")
        elif choice == "7" and cookies >= 4000:
            clear()
            actual_upgrades["click_power"] += 250
            cookies -= 4000
            print("Successfully bought")
        elif choice == "8" and cookies >= 250:
            clear()
            actual_upgrades["autoclicks"] *= 1.33
            cookies -= 250
            print("Successfully bought")
        elif choice == "9" and cookies >= 500:
            clear()
            actual_upgrades["click_power"] *= 1.33
            cookies -= 250
            print("Successfully bought")
        elif choice == "10" and cookies >= 6000:
            clear()
            actual_upgrades["click_power"] += 400
            cookies -= 6000
            print("Successfully bought")
        elif choice == "11" and cookies >= 3500:
            clear()
            actual_upgrades["autoclicks"] *= 2
            cookies -= 3500
            print("Successfully bought")
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
    clear()
    while True:
        print("Python cookie clicker")
        print(f"You have {cookies:.2f} cookies")
        print("Options:")
        print("Enter => Click cookie")
        print("1     => Visit shop")
        print("2     => View cookie data")
        print("3     => Quit")
        choice = input("> ").strip()
        if not bool(choice):
            clear()
            cookies += actual_upgrades["click_power"]
            print(f"+{actual_upgrades['click_power']} cookie(s)")
        elif choice == "1":
            upgrade_shop()
        elif choice == "2":
            clear()
            print(f"Click power: {actual_upgrades['click_power']:.2f}/click")
            print(f"Clicks per second: {actual_upgrades['autoclicks']:.2f}/s")
        elif choice == "3":
            break
        else:
            clear()
            print("Invalid input")
    print("bai")


if __name__ == "__main__":
    main()
