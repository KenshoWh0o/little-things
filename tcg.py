import random

# Définition des cartes Pokémon
Salameche = "Salameche, 30 PV, *"
Reptincel = "Reptincel, 60 PV, **"
Dracaufeu = "Dracaufeu, 120 PV, ***"
DracaufeuEx = "Dracaufeu EX, 180 PV, ****"
Carapuce = "Carapuce, 30 PV, *"
Carabaffe = "Carabaffe, 60 PV, **"
Tortank = "Tortank, 120 PV, ***"
TortankEx = "Tortank EX, 180 PV, ****"
Bulbizarre = "Bulbizarre, 30 PV, *"
Herbizarre = "Herbizarre, 60 PV, **"
Florizarre = "Florizarre, 120 PV, ***"
FlorizarreEx = "Florizarre EX, 180 PV, ****"

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
    print("Bienvenue dans le jeu de cartes Pokémon !")
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

