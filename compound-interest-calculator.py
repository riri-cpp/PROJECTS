principle = 0
rate = 0
time = 0

while principle <= 0:
    print("")
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("PRINCIPLE AMOUNT CAN'T BE LESS THAN OR EQUAL TO ZERO.")

while rate <= 0:
    print("")
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("INTEREST RATE CAN'T BE LESS THAN OR EQUAL TO ZERO.")

while time <= 0:
    print("")
    time = int(input("Enter the amount of time (in years): "))
    if time <= 0:
        print("AMOUNT OF TIME CAN'T BE LESS THAN OR EQUAL TO ZERO.")

total = principle * pow((1 + rate/100), time)

print(f"BALANCE AFTER {time} year/s: ${total:.2f}")
