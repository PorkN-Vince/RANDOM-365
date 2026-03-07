def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid Operator!"
    

if __name__ == "__main__":
    print("Simple Calculator")
    print("Operators: *   -   +   /")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter Operator!")
        num2 = float(input("Enter second number: "))


        result = calculate(num1, operator, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please input valid numbers.")
        
