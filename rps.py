import random

choices = ("rock", "paper", "scissors")
playerPoints = 0
computerPoints = 0

print()
print("------- ROCK PAPER SCISSORS -------")
print()

while True:
    computerChoice = random.choice(choices)
    print("PRESS [Q] TO QUIT ANYTIME")
    print()
    userChoice = input("Type [rock], [paper], or [scissors]: ").lower()
    if userChoice == "q":
        break
    elif userChoice not in choices:
        print("Please try again.")
        print()
    elif userChoice == computerChoice:
        print()
        print(f"Player: {userChoice}")
        print(f"Computer: {computerChoice}")
        print()
        print("It's a tie")
        print()
    elif userChoice == "rock" and computerChoice == "scissors":
        print()
        print(f"Player: {userChoice}")
        print(f"Computer: {computerChoice}")
        print()
        print("Player wins")
        print()
        playerPoints += 1
    elif userChoice == "paper" and computerChoice == "rock":
        print()
        print(f"Player: {userChoice}")
        print(f"Computer: {computerChoice}")
        print()
        print("Player wins")
        print()
        playerPoints += 1
    elif userChoice == "scissors" and computerChoice == "paper":
        print()
        print(f"Player: {userChoice}")
        print(f"Computer: {computerChoice}")
        print()
        print("Player wins")
        print()
        playerPoints += 1
    else:
        print()
        print(f"Player: {userChoice}")
        print(f"Computer: {computerChoice}")
        print()
        print("Computer wins")
        print()
        computerPoints += 1

print()
print("----------- FINAL SCORES -----------")
print()
print(f"Player Score: {playerPoints}")
print(f"Computer Score: {computerPoints}")
print()
print("------------------------------------")