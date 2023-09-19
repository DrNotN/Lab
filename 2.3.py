try:
    # Prompt the user to enter the population of the universe
    population = int(input("Enter the population of the universe: "))

    # Check if the population is an odd number
    if population % 2 == 1:
        # If odd, round up the number of survivors
        survivors = (population + 1) // 2
    else:
        # If even, half of the population will survive
        survivors = population // 2

    # Display the number of survivors
    print(f"Number of survivors: {survivors}")

except ValueError:
    print("Invalid input. Please enter a valid integer for the population.")
except Exception as e:
    print(f"An error occurred: {e}")
