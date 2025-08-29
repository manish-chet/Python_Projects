# When the program runs, it will randomly choose a number between 1 and 6. T
# When program will print what that number is. It should then ask you if you’d like to roll again.

# Output
    # Dice1: 3 
    # Dice2: 6
    # Roll the dice again? (Y/N)


import random 

rollagain = "Y"

while rollagain.upper() == "Y":
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice1: {dice1} \nDice2: {dice2}")
    rollagain = input("Roll the dice again? (Y/N): ")

    