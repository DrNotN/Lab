try:
    # Prompt the user to enter a four-digit number
    number = int(input("Enter a four-digit number: "))

    # Check if the entered number is indeed a four-digit number
    if 1000 <= number <= 9999:
        # Extract individual digits using integer division and modulo operator
        thousands = number // 1000
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        ones = number % 10

        # Display the individual digits
        print(f"Thousands digit: {thousands}")
        print(f"Hundreds digit: {hundreds}")
        print(f"Tens digit: {tens}")
        print(f"Ones digit: {ones}")
    else:
        print("Please enter a valid four-digit number.")

except ValueError:
    print("Invalid input. Please enter a valid four-digit number.")
except Exception as e:
    print(f"An error occurred: {e}")
