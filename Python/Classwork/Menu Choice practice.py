# # User-defined function
# def menu():
#     while True:
#         # Print the menu
#         print("\nMenu Driven Program")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Modulo")
#         print("6. Exit")

#         # Get user input
#         choice = input("Enter your choice (1-6): ")

#         # Exit condition
#         if choice == '6':
#             print("Exiting program.")
#             break

#         # Invalid choice check
#         if choice not in ['1', '2', '3', '4', '5']:
#             print("Invalid choice. Try again.")
#             exit()
#             continue

#         # Get two numbers, handle input errors
#         try:
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter numeric values.")
#             continue

#         # Perform selected operation
#         if choice == '1':
#             print(f"Result: {a + b}")
#         elif choice == '2':
#             print(f"Result: {a - b}")
#         elif choice == '3':
#             print(f"Result: {a * b}")
#         elif choice == '4':
#             if b == 0:
#                 print("Error: Cannot divide by zero.")
#             else:
#                 print(f"Result: {a / b}")
#         elif choice == '5':
#             if b == 0:
#                 print("Error: Cannot modulo by zero.")
#             else:
#                 print(f"Result: {a % b}")
#         exit()
# # Use for loop

# # Run the function
# menu()

# =================================================================================================================================
# =================================================================================================================================

# User-defined function
def menu():
    while True:
        # Print the menu
        print("\nMenu Driven Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("6. Exit")

        # Get user input
        choice = input("Enter your choice (1-6): ")

        # Exit condition
        if choice == '6':
            print("Exiting program...")
            break

        # Invalid choice check
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Try again.")
            exit()
            continue

        # Get two numbers, handle input errors
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform selected operation
        if choice == '1':
            print(f"Result: {a + b}")
        elif choice == '2':
            print(f"Result: {a - b}")
        elif choice == '3':
            print(f"Result: {a * b}")
        elif choice == '4':
            if b == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {a / b}")
        elif choice == '5':
            if b == 0:
                print("Error: Cannot modulo by zero.")
            else:
                print(f"Result: {a % b}")
        exit()
    # For loop runs after exiting the while loop
    print("\nThank you! Here's a quick countdown before exit:")
    for i in range(5, 0, -1):
        print(f"Closing in {i}...")
menu()