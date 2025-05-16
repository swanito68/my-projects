from liste_de_mots import mots
from os import system
import random as r

erreurs = 0
partiesGagnées = 0
partiesPerdues = 0
listeErreurs = []
listeBonneRéponses = []

asciiPendu = {
    0: (
        "    +-----┐",
        "    |     |",
        "          |",
        "          |",
        "          |",
        "          |",
        "   -------┴",
    ),
    1: (
        "    +-----┐",
        "    |     |",
        "    o     |",
        "          |",
        "          |",
        "          |",
        "   -------┴",
    ),
    2: (
        "    +-----┐",
        "    |     |",
        "    o     |",
        "    |     |",
        "          |",
        "          |",
        "   -------┴",
    ),
    3: (
        "    +-----┐",
        "    |     |",
        "    o     |",
        "   ⟋|     |",
        "          |",
        "          |",
        "   -------┴",
    ),
    4: (
        "    +-----┐",
        "    |     |",
        "    o     |",
        "   ⟋|⟍    |",
        "          |",
        "          |",
        "   -------┴",
    ),
    5: (
        "    +-----┐",
        "    |     |",
        "    o     |",
        "   ⟋|⟍    |",
        "   /      |",
        "          |",
        "   -------┴",
    ),
    6: (
        "    +-----┐",
        "    |     |",
        "    o     |",
        "   ⟋|⟍    |",
        "   / \\    |",
        "          |",
        "   -------┴",
    ),
}


def afficherPendu(viesUsées):
    print("**************")
    for ligne in asciiPendu[viesUsées]:
        print(ligne)
    print("**************")


def bulletin():
    print(f"Parties gagnées: {partiesGagnées}")
    print(f"Parties perdues: {partiesPerdues}")
    print("Essais incorrects:", listeErreurs, end=" ")
    print()


def main():
    global erreurs, partiesGagnées, partiesPerdues
    system("clear")
    print("Bienvenue au jeu de pendu")
    running = True
    a = 0
    while running:
        choix_mot = r.choice(mots)
        mot_masqué = ["_ "] * len(choix_mot)
        while a == 0:
            afficherPendu(erreurs)
            print(mot_masqué)
            entrée_util = input("Votre devinette: ")
            if len(entrée_util) != 1:
                system("clear")
                print("Vous ne pouvez pas mettre plus d'une lettre")
            elif not entrée_util.isalpha():
                system("clear")
                print("Votre entrée n'est pas une lettre de l'alphabet")
            else:
                if entrée_util in choix_mot:
                    for i in range(len(choix_mot)):
                        if choix_mot[i] == entrée_util:
                            mot_masqué[i] = entrée_util
                    if entrée_util not in listeBonneRéponses:
                        listeBonneRéponses.append(entrée_util)
                        system("clear")
                        print("Bonne réponse!")
                    else:
                        system("clear")
                        print("Vous avez déja deviné ceci")

                    if "_ " not in mot_masqué:
                        partiesGagnées += 1
                        print("Tu as gagné! :D")
                        bulletin()
                        a += 1
                else:
                    erreurs += 1
                    if entrée_util not in listeErreurs:
                        listeErreurs.append(entrée_util)
                    system("clear")
                    print(f"Mauvaise réponse! Il vous reste {6 - erreurs} vies")
                    if erreurs == 6:
                        print("Tu as perdu! :(")
                        bulletin()
                        a += 1
        while True:
            match input("Rejouer? ([O]ui/[N]on): ").strip().lower():
                case "o" | "oui":
                    system("clear")
                    listeBonneRéponses.clear()
                    listeErreurs.clear()
                    erreurs = 0
                    print("Rejouer")
                    a = 0
                    break
                case "n" | "non":
                    running = False
                    break
                case _:
                    system("clear")
                    print("Ce n'est pas une réponse valide")
    print("bai")


if __name__ == "__main__":
    main()
