import os
import string
from random import shuffle


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


characters = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = characters.copy()
shuffle(key)

encryption_dict = dict(zip(characters, key))
decryption_dict = dict(zip(key, characters))


def encrypt(text: str):
    encrypted = ""
    for char in text:
        encrypted += encryption_dict.get(char, char)
    return encrypted


def decrypt(text: str):
    decrypted = ""
    for char in text:
        decrypted += decryption_dict.get(char, char)
    return decrypted


def main():
    clear()
    print("Python encryption program")
    while True:
        try:
            print("\n1 -> Encrypt text")
            print("2 -> Decrypt text")
            print("3 -> See the key and the characters")
            print("4 -> Exit")
            choice = input("==> ").strip()
            if choice == "4":
                break
            elif choice == "1":
                clear()
                print("Text encryption")
                text_input = input("Your text here:\n=> ")
                encrypted_text = encrypt(text_input)
                clear()
                print(f"Encrypted text:\n'{encrypted_text}'")
                continue
            elif choice == "2":
                clear()
                print("Text decryption")
                text_input = input("Your text here:\n=> ")
                decrypted_text = decrypt(text_input)
                clear()
                print(f"Decrypted text:\n'{decrypted_text}'")
                continue
            elif choice == "3":
                clear()
                print(f"Characters: {characters}")
                print(f"Key: {key}")
                continue
            else:
                clear()
                print("Invalid input\n")
        except KeyboardInterrupt:
            print()
            print("Ctrl+C pressed")
            break
    print("bai")


if __name__ == "__main__":
    main()
