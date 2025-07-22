# # Get two integer inputs from the user
# a = int(input("Enter first number (a): "))
# b = int(input("Enter second number (b): "))

# # Check the conditions
# if a == b or (a + b == 5) or (abs(a - b) == 5):
#     print("True")
# else:
#     print("False")
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# Function to validate integer input
def get_valid_integer(prompt):
    value = input(prompt)
    try:
        num = float(value)
        if num.is_integer():
            return int(num)
        else:
            print("Float values are not allowed. Please enter integer values only.")
            return None
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return None

# Get valid integer inputs
a = get_valid_integer("Enter first number (a): ")
b = get_valid_integer("Enter second number (b): ")

# Proceed only if both inputs are valid integers
if a is not None and b is not None:
    if a == b or (a + b == 5) or (abs(a - b) == 5):
        print("True")
    else:
        print("False")
else:
    print("Program terminated due to invalid input.")
