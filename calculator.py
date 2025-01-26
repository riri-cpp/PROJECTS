import math

print("************ CALCULATOR PROGRAM ************")
operator = input("Enter an operator to use (+), (-), (*), or (/): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The sum is {round(result, 2)}")

elif operator == "-":
    result = num1 - num2
    print(f"The difference is {round(result, 2)}")

elif operator == "*":
    result = num1 * num2
    print(f"The product is {round(result, 2)}")

elif operator == "/":
    result = num1 / num2
    print(f"The quotient is {round(result, 2)}")

else:
    print("Please choose a valid operator.")