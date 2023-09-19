try:
    # Prompt the user to enter the edge length of the cube
    edge_length = float(input())

    # Calculate the volume of the cube
    volume = edge_length ** 3

    # Calculate the surface area of the cube
    surface_area = 6 * (edge_length ** 2)

    # Display the results
    print(f"Volume of the cube: {volume}")
    print(f"Surface area of the cube: {surface_area}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
