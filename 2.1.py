try:
    # Prompt the user to enter the total number of tangerines (K) and the number of schoolchildren (N)
    N = int(input())
    K = int(input())

    # Calculate how many whole tangerines each student will get using integer division
    tangerines_per_student = K // N

    # Calculate how many whole tangerines will remain in the basket using the modulo operator
    remainder = K % N

    # Display the results
    print(f"{tangerines_per_student}")
    print(f"{remainder}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("The number of schoolchildren (N) cannot be zero.")
except Exception as e:
    print(f"An error occurred: {e}")
