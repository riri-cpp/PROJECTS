import random
diceRolls = 0
while True:
    dice = random.randint(1, 6)
    userInput = input("Would you like to roll the dice? [Y] or [N]: ").lower()
    if userInput == "n":
        break
    elif userInput == "y":
        print()
        print(f"You rolled a {dice}!")
        print()
        diceRolls += 1
    else:
        print()
        print("Invalid input, try again.")
        print()

print()
print(f"You rolled the dice {diceRolls} times.")