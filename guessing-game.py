import random

low = int(input("Enter the minimum range: "))
high = int(input("Enter the maximum range: "))
guess = 0

randnum = random.randint(low, high)

while True:
    print()
    playerGuess = int(input("Enter your guess: "))

    if playerGuess > randnum:
        print("Too high! Try again.")
        guess += 1
    elif playerGuess < randnum:
        print("Too low! Try again")
        guess += 1
    else:
        print(f"Correct! The number is {randnum}")
        print(f"You guessed {guess} times")
        break

exit()
