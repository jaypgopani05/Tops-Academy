# def first_last_2_chars(s):
#     if len(s) < 2:
#         return "String too short"
#     return s[:2] + s[-2:]

# # Example usage user input:

# input_str = input("Enter a string: ")
# result = first_last_2_chars(input_str)
# print("Result:", result)

# it accepts and returns the numeric and alphanumeric values as well.
# need to filter the string type more accutately.
# This code will also allows user to insert any int, float, numeric 
# or alphanumeric value and returns the first and last two characters of the string.

# ============================================================================================
# ============================================================================================

# # Get input from the user
# input_str = input("Enter a string (alphabets only): ")

# # Check if the input contains only alphabets
# if input_str.isalpha():
#     # Check if the string has at least 2 characters
#     if len(input_str) >= 2:
#         # Get first 2 and last 2 characters and combine
#         result = input_str[0] + input_str[1] + input_str[-2] + input_str[-1]
#         print("Result:", result)
#     else:
#         print("Error: String too short.")
# else:
#     print("Error: Please enter only alphabetic characters.")

# This code checks if the input string contains only alphabetic characters 
# and has at least 2 characters. 
# If both conditions are met, it returns the first 2 and last 2 characters combined.
# If the string is too short or contains non-alphabetic characters, 
# it displays an error message.

# However this code is using more basic and complex structure of code. need to filter the coding.
# ============================================================================================
# ============================================================================================

# This code defines a function that takes a string input and returns a new string

# def first_last_2_chars(s):
#     if not s.isalpha():
#         return "Error: Please enter alphabetic characters only."
#     if len(s) < 2:
#         return "Error: String too short."
#     return s[:2] + s[-2:]

# # Example usage
# input_str = input("Enter a string (alphabets only): ")
# result = first_last_2_chars(input_str)
# print("Result:", result)
# This code is not allowing spaces and only allows alphabetic characters withpout spaces between words.
# need to allow Space or any special characters as well. but do not count it as part of string.

# =============================================================================================
# =============================================================================================

# # Get input from user
# input_str = input("Enter text (no digits allowed): ")

# # Validate: Reject if any digit is in the input
# contains_digit = False
# for ch in input_str:
#     if ch.isdigit():
#         contains_digit = True
#         break

# if contains_digit:
#     print("Error: Digits are not allowed.")
# else:
#     # Filter out only valid characters (excluding digits and spaces)
#     filtered = ''
#     for ch in input_str:
#         if ch != ' ' and not ch.isdigit():
#             filtered += ch

#     if len(filtered) >= 2:
#         # Get first 2 and last 2 characters from the filtered string
#         result = filtered[0] + filtered[1] + filtered[-2] + filtered[-1]
#         print("Result:", result)
#     else:
#         print("Error: Not enough valid characters (excluding spaces and digits).")
#  This program works fine but t=it allows alphanumeric values like (1234 jay). We need to allow that in user input.
# However we are restricting only digit inputs from user so need to filter more accurately.

# ==================================================================================================
# ==================================================================================================

# Get user input
input_str = input("Enter text (cannot be digits only, spaces allowed): ")

# Check: Input must not be digits only (after removing spaces)
without_spaces = ''
for char in input_str:
    if char != ' ':
        without_spaces += char

if without_spaces.isdigit():
    print("Error: Input cannot contain only digits.")
else:
    # Collect all non-space characters
    valid_chars = ''
    for ch in input_str:
        if ch != ' ':
            valid_chars += ch

    if len(valid_chars) >= 2:
        # Get first 2 and last 2 non-space characters
        result = valid_chars[0] + valid_chars[1] + valid_chars[-2] + valid_chars[-1]
        print("Result:", result)
    else:
        print("Error: Not enough non-space characters.")
# This code allows spaces in the input but does not allow the input to be only digits.
# It collects all non-space characters and returns the first 2 and last 2 characters.
# It also checks if there are enough non-space characters to perform the operation.
# This code is working perfectly fine and allows user to input any alphanumeric value with spaces in between.
# Also keep the spaces between words intact while returning the first and last two characters of the string. And Summing up final result.