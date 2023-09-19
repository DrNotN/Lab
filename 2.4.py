try:
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))

    # Perform a left bitwise shift operation by 1
    result = num << 1

    # Check if the result is zero
    if result == 0:
        print("Warning: The result of the left shift operation is zero.")
    else:
        print(f"Result of left shift operation: {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")