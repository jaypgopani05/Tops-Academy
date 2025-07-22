# # Get input from the user
# n = int(input("Enter a positive integer (n): "))

# # Check if the number is positive
# if n <= 0:
#     return "Please enter a positive integer."
# else:
#     # Using the formula: sum = n * (n + 1) // 2
#     total = n * (n + 1) // 2
#     print(f"The sum of the first {n} positive integers is {total}.")
# ============================================================================================
# ============================================================================================
# ============================================================================================



















# Function to validate integer input
def get_positive_integer():
    user_input = input("Enter a positive integer (n): ")
    try:
        num = float(user_input)

        # Check for float (non-integer)
        if not num.is_integer():
            print("Float values are not allowed. Please enter an integer only.")
            return None

        # Convert to integer after confirming it's whole
        num = int(num)

        # Check if it's positive
        if num <=0:
            print("Only positive integers are allowed.")
            return None

        return num

    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return None

# Get valid input
n = get_positive_integer()

# If input is valid, perform the sum
if n is not None:
    total = n * (n + 1) // 2
    print(f"The sum of the first {n} positive integers is {total}.")
else:
    print("Program terminated due to invalid input.")
# ================================================================================================
