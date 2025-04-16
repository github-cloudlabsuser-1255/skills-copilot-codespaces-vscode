def calculator():
    """
    This script provides a simple calculator program that allows users to perform basic arithmetic operations.
    Functions:
        calculator():
            - Displays a menu of operations: Add, Subtract, Multiply, Divide, Percentage, and Exit.
            - Prompts the user to select an operation and input numbers as required.
            - Performs the selected operation and displays the result.
            - Handles invalid inputs and division by zero errors gracefully.
            - Loops until the user chooses to exit.
    Usage:
        Run the script and follow the prompts to perform calculations.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    # Take input from the user
    print("6. Exit")
    choice = input("Enter choice (1/2/3/4/5/6): ")
    while choice != '6':
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                if choice == '5':
                    # For percentage, only one number is needed
                    print(f"The result is: {num1 / 100}")
                else:
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(f"The result is: {num1 + num2}")
                    elif choice == '2':
                        print(f"The result is: {num1 - num2}")
                    elif choice == '3':
                        print(f"The result is: {num1 * num2}")
                    elif choice == '4':
                        if num2 != 0:
                            print(f"The result is: {num1 / num2}")
                        else:
                            print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")
        
            print("\nSelect operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Percentage")
            print("6. Exit")
            choice = input("Enter choice (1/2/3/4/5/6): ")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()