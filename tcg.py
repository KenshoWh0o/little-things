#PokePython
#A program that simulates opening Pokémon booster packs.

import random
import sys
sys.path.append('')

# Variables
Charmander = "#1 - Charmander - *"
Charmelon = "#2 - Charmelon - **"
Charizard = "#3 - Charizard - ***"
CharizardEx = "#4 - Charizard EX - ****"
Squirtle = "#5 - Squirtle - *"
Wartortle = "#6 - Wartortle - **"
Blastoise = "#7 - Blastoise - ***"
BlastoiseEx = "#8 - Blastoise EX - ****"
Bulbasaur = "#9 - Bulbasaur - *"
Ivysaur = "#10 - Ivysaur - **"
Venusaur = "#11 - Venusaur - ***"
VenusaurEx = "#12 - Venusaur EX - ****"
Caterpie = "#13 - Caterpie - *"
Metapod = "#14 - Metapod - **"
Butterfree = "#15 - Butterfree - ***"
Weedle = "#16 - Weedle - *"
Kakuna = "#17 - Kakuna - **"
Beedrill = "#18 - Beedrill - ***"
Pidgey = "#19 - Pidgey - *"
Pidgeotto = "#20 - Pidgeotto - **"
Pidgeot = "#21 - Pidgeot - ***"
Rattata = "#22 - Rattata - *"
Raticate = "#23 - Raticate - **"
Pikachu = "#24 - Pikachu - *"
Raichu = "#25 - Raichu - **"
PikachuEx = "#26 - Pikachu EX - ***"
Psyduck = "#27 - Psyduck - *"
Golduck = "#28 - Golduck - **"
Abra = "#29 - Abra - *"
Kadabra = "#30 - Kadabra - **"
Alakazam = "#31 - Alakazam - ***"
AlakazamEx = "#32 - Alakazam EX - ****"
Magikarp = "#33 - Magikarp - *"
Gyarados = "#34 - Gyarados - ***"
GyaradosEx = "#35 - Gyarados EX - ****"
Snorlax = "#36 - Snorlax - ***"
SnorlaxEx = "#37 - Snorlax EX - ****"
Dratini = "#38 - Dratini - *"
Dragonair = "#39 - Dragonair - **"
Dragonite = "#40 - Dragonite - ***"
DragoniteEx = "#41 - Dragonite EX - ****"
Mewto = "#42 - Mewto - ***"
MewtoEx = "#43 - Mewto EX - ****"
Mew = "#44 - Mew - ***"
MewEx = "#45 - Mew EX - *****"


# Lists
pokemons = [Charmander, Squirtle, Bulbasaur, Caterpie, Weedle, Pidgey, Rattata, Pikachu, Psyduck, Abra, Magikarp, Dratini, Charmelon, Wartortle, Ivysaur, Metapod, 
            Kakuna, Pidgeotto, Raticate, Raichu, Golduck, Kadabra, Dragonair, Charizard, Blastoise, Venusaur, Butterfree, Beedrill, Pidgeot, Alakazam, Gyarados, Snorlax, Dragonite, 
            Mew, Mewto, CharizardEx, BlastoiseEx, VenusaurEx, PikachuEx, AlakazamEx, GyaradosEx, SnorlaxEx, DragoniteEx, MewtoEx, MewEx]
pokemon1star = pokemons[0:12]
pokemon2star = pokemons[12:23]
pokemon3star = pokemons[23:35]
pokemon4star = pokemons[35:44]
pokemon5star = pokemons[44:45]

# Functions obtaining random cards
def random_pokemon1star():
    return random.choice(pokemon1star)
def random_pokemon2star():
    return random.choice(pokemon2star)
def random_pokemon3star():
    return random.choice(pokemon3star)
def random_pokemon4star():
    return random.choice(pokemon4star)
def random_pokemon5star():
    return random.choice(pokemon5star)

# Functions opening a booster

    # Function opening a god pack
def godpack():
    print()
    input("There are the cards you obtained (press Enter to see the next card) :")
    input("GOD PACK !")
    input(random_pokemon3star())
    input(random_pokemon3star())
    input(random_pokemon4star())
    input(random_pokemon4star())
    input(random_pokemon5star())
    input()
    menu()

    # Function opening a base pack
def basepack():
    print()
    input("There are the cards you obtained (press Enter to see the next card) :")
    input(random_pokemon1star())
    if random.randint(1, 2) == 1 :
        input(random_pokemon1star())
    else :
        input(random_pokemon2star())
    if random.randint(1, 2) == 1 :
        input(random_pokemon2star())
    else :
        input(random_pokemon3star())
    input(random_pokemon3star())
    if random.randint(1, 50) == 1 :
        input(random_pokemon5star())
    elif random.randint(1, 10) == 1 :
        input(random_pokemon4star())
    else :
        input(random_pokemon3star())
    input()
    menu()

    # Function choosing if opening a god pack or a base pack
def booster():
    if random.randint(1, 100) == 1:
        godpack()
    else:
        basepack()

# Function displaying every pokemon
def showallpokemons():
    print()
    print("There is the list of every pokemon (press Enter to go back to menu) :")
    print()
    for pokemon in pokemons:
        print(pokemon)
    input()
    menu()

# Function displaying the menu
def menu():
    print("====")
    print("Menu")
    print("====")
    print()
    print("1. Open a booster")
    print("2. Display every pokemon")
    print("3. Leave")
    choice = input("Your choice : ")
    if choice == "1":
        booster()
    elif choice == "2":
        showallpokemons()
    elif choice == "3":
        print()
        print("Thanks for playing !")
    else:
        print("Incorrect choice. Please try again.")
        menu()

# Function launching the game
def launch():
    print("=======================")
    print("Welcome to PokePython !")
    print("=======================")
    print()
    print("To see the menu, please press Enter")
    input()
    menu()

# Calling the launching function
launch()