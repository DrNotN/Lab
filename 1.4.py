try:
    # Prompt the user to enter three integers, each on a separate line
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    # Calculate the sum of the three integers
    total_sum = num1 + num2 + num3

    # Display the sum on the screen
    print(f"{total_sum}")

except ValueError:
    print("Invalid input. Please enter valid integers.")
except Exception as e:
    print(f"An error occurred: {e}")