# The Sorting Hat
# A program that asks a series of questions to determine which house you belong to in the Harry Potter universe.

# Variables
s = 0
h = 0
r = 0
g = 0

# Title
print("===============")
print("The Sorting Hat")
print("===============")


# Question 1
print("Q1) Do you like Dawn or Dusk ?")
print("   1) Dawn")
print("   2) Dusk")

answer = int(input('Type your answer'))

if answer == 1 :
  g += 1
  r += 1
elif answer == 2 :
  h += 1
  s += 1
else :
  print("Wrong input")


# Question 2
print("\nQ2) When I’m dead, I want people to remember me as :")
print("   1) The Good")
print("   2) The Great")
print("   3) The Wise")
print("   4) The Bold")

answer = int(input('Type your answer'))

if answer == 1 :
  h += 2
elif answer == 2 :
  s += 2
elif answer == 3 :
  r += 2
elif answer == 4 :
  g += 2
else :
  print("Wrong input")


# Question 3
print("\nQ3) Which kind of instrument most pleases your ear ?")
print("   1) The violin")
print("   2) The trumpet")
print("   3) The piano")
print("   4) The drum")

answer = int(input('Type your answer'))

if answer == 1 :
  s += 4
elif answer == 2 :
  h += 4
elif answer == 3 :
  r += 4
elif answer == 4 :
  g += 4
else :
  print("Wrong input")


# Results
print("\nYou are a...")
if s > h and s > r and s > g :
  print ("Slytherin !")
elif h > s and h > r and h > g :
  print("Hufflepuff")
elif r > h and r > s and r > g :
  print("Ravenclaw !")
elif g > r and g > h and g > s :
  print("Gryffindor !")