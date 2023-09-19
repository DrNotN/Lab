try:
    # Prompt the user to enter the first number
    user_input = input()

    # Attempt to convert the user input to an integer
    first_number = int(user_input)

    # Calculate the second and third consecutive numbers
    second_number = first_number + 1
    third_number = first_number + 2

    # Display the consecutive numbers on separate lines
    print(f"\n{first_number}\n{second_number}\n{third_number}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")