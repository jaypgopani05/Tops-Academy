# # Get input from the user
# input_str = input("Enter a string: ")

# # Check length of the string
# if len(input_str) < 3:
#     result = input_str
#     print("String is too short, returning original string:", result)
# elif input_str.endswith("ing"):
#     result = input_str + "ly"
#     print("String ends with 'ing', adding 'ly':", result)
# else:
#     result = input_str + "ing"
# # Display the result
# print("Modified string:", result)

# ==========================================================================================
# ==========================================================================================

# New Program with updates also checks and allows user to input only string 
# and rejects number input by user. Example: 123, 1234, 12.34, etc. 
# Python will throw an error if we try to use string methods on numbers.

# ===========================================================================================
# ============================================================================================

# Get input from the user
# input_str = input("Enter a string: ")

# Validate: reject input if it's fully numeric
# if input_str.isnumeric():
#     print("Invalid input! Numbers are not allowed. Please enter a valid String.")
# else:
#     # Check length of the string
#     if len(input_str) < 3:
#         result = input_str
#         print("String is too short, returning original string:", result)
#         print("Note: The string must be at least 3 characters long to modify it.")
#     elif input_str.endswith("ing"):
#         result = input_str + "ly"
#         print("String ends with 'ing', adding 'ly':", result)
#     else:
#         result = input_str + "ing"

#     # Display the result
#     print("Modified string:", result)

    # Still shows the modified string result even if the input was too short or gets any error from user input.
    # Updating the code to handle errors gracefully.

# ============================================================================================
# ============================================================================================
# ============================================================================================

# New Program with updates also checks and allows user to input only string
# and rejects number input by user. Example: 123, 1234, 12.34, etc.
# Python will throw an error if we try to use string methods on numbers. 
# Also Do not show modified string result if the input was too short or gets any error from user input.

# ============================================================================================
# ============================================================================================


# Get input from the user
input_str = input("Enter a string: ")

# Validate: reject fully numeric input
if input_str.isnumeric():
    print("Invalid input! Numbers are not allowed. Please enter a valid word.")
    
# Check if the string is too short
elif len(input_str) < 3:
    print("String is too short. Minimum length should be 3 characters.")

# Valid string, proceed with logic
else:
    if input_str.endswith("ing"):
        result = input_str + "ly"
        print("String ends with 'ing', adding 'ly' at the end.\n " "New Modified String Is:", result)
    else:
        result = input_str + "ing"
        print("Modified string:", result)
# Note: The string must be at least 3 characters long to modify it. Do not show modified string result if the input was too short or gets any error from user input.
# ============================================================================================
# ============================================================================================