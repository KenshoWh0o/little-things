#PokePython
#A program that simulates opening Pokémon booster packs.

import random

# Définition des cartes Pokémon
Salameche = "#1 - Salameche - *"
Reptincel = "#2 - Reptincel - **"
Dracaufeu = "#3 - Dracaufeu - ***"
DracaufeuEx = "#4 - Dracaufeu EX - ****"
Carapuce = "#5 - Carapuce - *"
Carabaffe = "#6 - Carabaffe - **"
Tortank = "#7 - Tortank - ***"
TortankEx = "#8 - Tortank EX - ****"
Bulbizarre = "#9 - Bulbizarre - *"
Herbizarre = "#10 - Herbizarre - **"
Florizarre = "#11 - Florizarre - ***"
FlorizarreEx = "# 12 - Florizarre EX - ****"


# Définition des boosters
pokemons = [Salameche, Carapuce, Bulbizarre, Reptincel, Carabaffe, Herbizarre, 
            Dracaufeu, Tortank, Florizarre, DracaufeuEx, TortankEx, FlorizarreEx]
pokemon1star = pokemons[0:3]
pokemon2star = pokemons[3:6]
pokemon3star = pokemons[6:9]
pokemon4star = pokemons[9:12]

# Fonctions pour obtenir des cartes aléatoires
def random_pokemon1star():
    return random.choice(pokemon1star)
def random_pokemon2star():
    return random.choice(pokemon2star)
def random_pokemon3star():
    return random.choice(pokemon3star)
def random_pokemon4star():
    return random.choice(pokemon4star)

# Fonction pour obtenir un booster complet
def godpack():
    print()
    input("Voici les cartes que vous avez obtenues (appuyez sur Entrée pour passer à la carte suivante) :")
    input(random_pokemon2star())
    input(random_pokemon3star())
    input(random_pokemon3star())
    input(random_pokemon4star())
    input(random_pokemon4star())
    input()
    menu()

def basepack():
    print()
    input("Voici les cartes que vous avez obtenues (appuyez sur Entrée pour passer à la carte suivante) :")
    input(random_pokemon1star())
    input(random_pokemon1star())
    input(random_pokemon2star())
    input(random_pokemon2star())
    if random.randint(1, 5) == 1 :
        input(random_pokemon4star())
    elif random.randint(1, 2) == 1 :
        input(random_pokemon3star())
    else :
        input(random_pokemon2star())
    input()
    menu()

def booster():
    if random.randint(1, 100) == 1:
        godpack()
    else:
        basepack()

# Fonction pour afficher tous les pokémons
def showallpokemons():
    print()
    print("Voici la liste de tous les pokémons (appuyez sur Entrée pour retourner au menu) :")
    print()
    print(Salameche)
    print(Reptincel)
    print(Dracaufeu)
    print(DracaufeuEx)
    print(Carapuce)
    print(Carabaffe)
    print(Tortank)
    print(TortankEx)
    print(Bulbizarre)
    print(Herbizarre)
    print(Florizarre)
    print(FlorizarreEx)
    input()
    menu()

# Fonction pour afficher le menu
def menu():
    print("====")
    print("Menu")
    print("====")
    print()
    print("1. Ouvrir un booster")
    print("2. Afficher tous les pokémons")
    print("3. Quitter")
    choice = input("Votre choix : ")
    if choice == "1":
        booster()
    elif choice == "2":
        showallpokemons()
    elif choice == "3":
        print()
        print("Merci d'avoir joué !")
    else:
        print("Choix invalide. Veuillez réessayer.")
        menu()

# Fonction pour lancer le jeu
def launch():
    print("=========================================")
    print("Bienvenue dans le jeu de cartes Pokémon !")
    print("=========================================")
    print()
    print("Pour vous diriger vers le menu, appuyez sur Entrée.")
    input()
    menu()

# Appel de la fonction pour lancer le jeu
launch()
