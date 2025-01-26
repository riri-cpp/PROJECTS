# collection practice

print()
print("****** SHOPPING CART PROGRAM ******")

items = []
prices = []

total = 0

while True:
    print()
    item = input("Enter the item you would like to buy (Press 'Q' to quit): ")
    if item in ["Q", "q"]:
        break
    else:
        print()
        price = float(input(f"Enter the price for {item}: PHP "))
        items.append(item)
        prices.append(price)

print()

print("--------- YOUR SHOPPING CART ---------")
items.sort

print()
for item in items:
    print(item)

for price in prices:
    total = price + total

print()
print(f"TOTAL COST: PHP {total:.2f}")