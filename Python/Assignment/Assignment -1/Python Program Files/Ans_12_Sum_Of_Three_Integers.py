# # Get three integer inputs from the user
# a = int(input("Enter first number (a): "))
# b = int(input("Enter second number (b): "))
# c = int(input("Enter third number (c): "))

# # Check if any two values are equal
# if a == b or b == c or a == c:
#     sum_result = 0
# else:
#     sum_result = a + b + c

# # Display the result
# print("The result is:", sum_result)
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

# Function to check if a number is an integer
def is_valid_integer(value):
    try:
        # Convert to float to check decimal part
        num = float(value)
        if num.is_integer():  # Ensure it's a whole number
            return int(num)
        else:
            print("Float values are not allowed! Please enter integers only.")
            return None
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return None

# Get inputs from the user
a_input = input("Enter first number (a): ")
b_input = input("Enter second number (b): ")
c_input = input("Enter third number (c): ")

# Validate all inputs
a = is_valid_integer(a_input)
b = is_valid_integer(b_input)
c = is_valid_integer(c_input)

# If all inputs are valid integers, proceed
if a is not None and b is not None and c is not None:
    if a == b or b == c or a == c:
        sum_result = 0
    else:
        sum_result = a + b + c
    print("The result is:", sum_result)
else:
    print("Program terminated due to invalid input.")
