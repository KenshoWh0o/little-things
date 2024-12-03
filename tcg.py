import random

# Définition des cartes Pokémon
Salameche = "Salameche - *"
Reptincel = "Reptincel - **"
Dracaufeu = "Dracaufeu - ***"
DracaufeuEx = "Dracaufeu EX - ****"
Carapuce = "Carapuce - *"
Carabaffe = "Carabaffe - **"
Tortank = "Tortank - ***"
TortankEx = "Tortank EX - ****"
Bulbizarre = "Bulbizarre - *"
Herbizarre = "Herbizarre - **"
Florizarre = "Florizarre - ***"
FlorizarreEx = "Florizarre EX - ****"
Chenipan = "Chenipan - *"
Chrysacier = "Chrysacier - **"
Papilusion = "Papilusion - ***"


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

# Fonction principale
def main():
    print("=========================================")
    print("Bienvenue dans le jeu de cartes Pokémon !")
    print("=========================================")
    print()
    print("Pour ouvrir un booster, appuyez sur Entrée.")
    input()
    print("Voici les cartes que vous avez obtenues :")
    print(random_pokemon1star())
    print(random_pokemon1star())
    print(random_pokemon2star())
    print(random_pokemon2star())
    if random.randint(1, 2) == 1 :
        print(random_pokemon4star())
    else :
        print(random_pokemon3star())

# Appel de la fonction principale
main()

