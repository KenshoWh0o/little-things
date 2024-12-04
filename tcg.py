#PokePython
#A program that simulates opening Pokémon booster packs.

import random

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
VenusaurEx = "# 12 - Venusaur EX - ****"


# Lists
pokemons = [Charmander, Squirtle, Bulbasaur, Charmelon, Wartortle, Ivysaur, 
            Charizard, Blastoise, Venusaur, CharizardEx, BlastoiseEx, VenusaurEx]
pokemon1star = pokemons[0:3]
pokemon2star = pokemons[3:6]
pokemon3star = pokemons[6:9]
pokemon4star = pokemons[9:12]

# Functions obtaining random cards
def random_pokemon1star():
    return random.choice(pokemon1star)
def random_pokemon2star():
    return random.choice(pokemon2star)
def random_pokemon3star():
    return random.choice(pokemon3star)
def random_pokemon4star():
    return random.choice(pokemon4star)

# Functions opening a booster
def godpack():
    print()
    input("There are the cards you obtained (press Enter to see the next card) :")
    input(random_pokemon2star())
    input(random_pokemon3star())
    input(random_pokemon3star())
    input(random_pokemon4star())
    input(random_pokemon4star())
    input()
    menu()

def basepack():
    print()
    input("There are the cards you obtained (press Enter to see the next card) :")
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
