print("======================================")
print("       HOTEL MANAGEMENT SYSTEM        ")
print("======================================")

unit = "PHP"
juniorPrice = 240
seniorPrice = 420
hillPrice = 680

print("")
print("ROOM RATES: ")
print(f"{'Junior Suite:':20}{unit} {juniorPrice:.2f} per night.")
print(f"{'Senior Suite:':20}{unit} {seniorPrice:.2f} per night.")
print(f"{'Hillside Villa:':20}{unit} {hillPrice:.2f} per night.")
print("")

choice = input("Press [1] to book now, [2] to exit: ")

if choice == "1":
    print("")
    print("======================================")
    print("           BOOKING SYSTEM             ")
    print("======================================")
    print("")

    while choice == "1":
        print("ROOM SELECTION:")
        print(f"{'[A]':3} Junior Suite")
        print(f"{'[B]':3} Senior Suite")
        print(f"{'[C]':3} Hillside Villa")
        print("")
        roomChoice = input("Enter room of choice: ")

        if roomChoice in ["A", "a"]:
            print("")
            print(f"Junior Suite: {unit} {juniorPrice:.2f} per night.")
            break
        elif roomChoice in ["B", "b"]:
            print("")
            print(f"Senior Suite: {unit} {seniorPrice:.2f} per night.")
            break
        elif roomChoice in ["C", "c"]:
            print("")
            print(f"Hillside Villa: {unit} {hillPrice:.2f} per night.")
            break
        else:
            print("Invalid choice. Try again.")
            print("")

elif choice == "2":
    print("")
    print("THANK YOU FOR USING OUR HOTEL! PLEASE COME AGAIN!")
    exit()
else:
    print("")
    print("Invalid")
    exit()

print("")
print("ENTER CUSTOMER DETAILS: ")
print("")
name = input("Enter your Full Name [Juan de la Cruz]: ")
age = int(input("Enter your Age [20]: "))
contact = (input("Enter your Contact Number [09XXXXXXXXX]: "))
nights = int(input("Enter the number of Nights [2]: "))
budget = int(input("Enter your total budget [1000]: "))

if roomChoice in ["A", "a"]:
    totalPrice = juniorPrice * nights
elif roomChoice in ["B", "b"]:
    totalPrice = seniorPrice * nights
elif roomChoice in ["C", "c"]:
    totalPrice = hillPrice * nights

if budget < totalPrice:
    print("")
    print("You do not have enough money to afford that.")
    exit()

change = budget - totalPrice

print("")
print("======================================")
print("         SUCCESSFULLY BOOKED          ")
print("======================================")
print("")

print("CUSTOMER DETAILS: ")
print("")
print(f"{'NAME:':20} {name}")
print(f"{'AGE:':20} {age}")
print(f"{'CONTACT NUMBER:':20} {contact}")
print(f"{'NIGHT/S STAYING:':20} {nights}")
print(f"{'TOTAL BUDGET:':20} PHP {budget:.2f}")
print("")

print("PAYMENT DETAILS: ")
print("")
print(f"{'TOTAL COST:':15} PHP {totalPrice:.2f}")
print(f"{'TOTAL CHANGE:':15} PHP {change:.2f}")

print("")
print("THANK YOU FOR USING OUR HOTEL! PLEASE COME AGAIN!")
exit()