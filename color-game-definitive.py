import random

total_amount = 0
earned_amount = 0
colors_list = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'WHITE', 'VIOLET']

print("="*30)
print("          COLOR GAME          ")
print("="*30)
print()

main_choice = input("PRESS [Y] / [N] TO PLAY COLOR GAME: ").lower()
if main_choice == "y":
    print()
    your_money = int(input("Enter your money: $"))
elif main_choice == "n":
    exit()
else:
    print()
    print("INVALID CHOICE")
    exit()

print()

while True:

    rand1 = random.randint(0, 5)
    rand2 = random.randint(0, 5)
    rand3 = random.randint(0, 5)

    winning_color1 = colors_list[rand1]
    winning_color2 = colors_list[rand2]
    winning_color3 = colors_list[rand3]

    print("-"*46)
    print()
    choice = input("PRESS [Y] / [N] TO CONFIRM PLAY: ").lower()

    if choice == "n":
        did_play = True
        break
    elif choice == "y":
        print()
        print("COLOR SELECTION:", colors_list)
        print()
        chosen_color = input("Enter your color: ").upper()
        if chosen_color not in colors_list:
            print()
            print(f"{chosen_color.capitalize()} is not a valid color! Please try again.")
            print()
        else:
            print()
            starting_amount = int(input("Enter your bet: $"))
            starting_amount - your_money

            if starting_amount <= 0 or starting_amount > your_money:
                print()
                print("Invalid bet amount.")
                did_play = False
                break
            else:
                print()
                print(f"YOU BET {starting_amount:.2f} on {chosen_color.capitalize()}")
                print()

            print(f"WINNING COLORS: {winning_color1.upper()} / {winning_color2.upper()} / {winning_color3.upper()}")

            if chosen_color == winning_color1 and chosen_color == winning_color2 and chosen_color == winning_color3:
                print()
                print("YOU HIT A TRIPLE!")
                print(f"You earned ${starting_amount * 3}")
                print()

                earned_amount = starting_amount * 3
                your_money = your_money + earned_amount
                total_amount = total_amount + earned_amount
                did_play = True

            elif (chosen_color == winning_color1 and chosen_color == winning_color2) or (chosen_color == winning_color1 and chosen_color == winning_color3) or (chosen_color == winning_color2 and chosen_color == winning_color3):
                print()
                print(f"You won ${starting_amount * 2}!")
                print()

                earned_amount = starting_amount * 2
                your_money = your_money + earned_amount
                total_amount = total_amount + earned_amount
                did_play = True

            elif chosen_color == winning_color1 or chosen_color == winning_color2 or chosen_color == winning_color3:
                print()
                print(f"You won ${starting_amount}!")
                print()

                earned_amount = starting_amount
                your_money = your_money + earned_amount
                total_amount = total_amount + earned_amount
                did_play = True

            else:
                print()
                print(f"You lost ${starting_amount}!")
                print()

                your_money = your_money - starting_amount
                did_play = True

            if your_money <= 0:
                break
            else:
                continue

    else:
        print()
        print("Invalid input.")
        print()

print()
print("-"*46)
print()
print("GAME SUMMARY:")
print()

if did_play == True:
    print(f"Your money: ${your_money}")
    if total_amount > 0:
        print(f"You earned a total of ${total_amount}")
    elif total_amount == 0:
        print("No bets were placed.")
else:
    print("INVALID INPUT DETECTED. PLEASE TRY AGAIN")

exit()
