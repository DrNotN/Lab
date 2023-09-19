try:
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform the selected operation and display the result
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            result = num1 / num2
    else:
        print("Invalid operation. Please choose from addition, subtraction, multiplication, or division.")

    if operation in ["+", "-", "*", "/"]:
        print(f"{num1} {operation} {num2} = {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
