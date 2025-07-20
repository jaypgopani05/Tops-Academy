# # Define a function to print the pattern
# def pattern(rows):
#     for i in range(1, rows + 1):
#         for j in range(i):
#             print("*", end=" ")
#         print()  # Move to next line after each row

# # Take input from the user
# user_input = int(input("Enter the number of rows: "))

# Call the function
# pattern(user_input)
# --- end of code snippet ---
# This code takes a number of rows as input from the user and prints a pattern of asterisks.
# It uses nested loops to print the required number of asterisks in each row, incrementing the count with each new row.

# =================================================================================================================
# =================================================================================================================

# This code defines a function that prints a pattern of asterisks based on the number of rows specified by the user.
# It uses nested loops to print the required number of asterisks in each row, incrementing the count with each new row.
# =================================================================================================================

# def number_pattern(rows):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
# user_input = int(input("Enter the number of rows: "))
# number_pattern(user_input)
# This code takes a number of rows as input from the user and prints a pattern of numbers.
# It uses nested loops to print the required numbers in each row, incrementing the count with each new row. 

# =================================================================================================================
# =================================================================================================================

# def repeat_number_pattern(rows):
#     for i in range(1, rows + 1):
#         for j in range(i):
#             print(i, end=" ")
#         print()

# user_input = int(input("Enter the number of rows: "))
# repeat_number_pattern(user_input)

# This code takes a number of rows as input from the user and prints a pattern where each row contains the row number repeated.
# It uses nested loops to print the required number in each row, repeating it according to the row index.
# =================================================================================================================
# =================================================================================================================
def reverse_number_pattern(rows):
    for i in range(rows, 0, -1):
        # print(i)
        for j in range(1, i + 1):
            print(j, end=" ")
            # print(j)
        print()
user_input = int(input("Enter the number of rows: "))
reverse_number_pattern(user_input)
