#task4 calculator
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:  # Prevent division by zero
            print("Error: Division by zero")
            return
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    else:
        print("Invalid operator")
        return

    print("Result:", result)

# Run the calculator
calculator() 
