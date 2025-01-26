#dictionaries practice

print()
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")

while True:
    food = input("What would you like to order? (Press [Q] to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print()
print("------ YOUR ORDER ------")
for food in cart:
    total = total + menu.get(food)
    print(f"{food.capitalize()}")
print("------------------------")

print()
print(f"Your total is ${total:.2f}")
print()