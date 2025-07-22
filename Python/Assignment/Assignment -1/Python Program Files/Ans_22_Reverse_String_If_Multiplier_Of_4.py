# def reverse_if_multiple_of_4(s):
#     if len(s) % 4 == 0:
#         return s[::-1]
#     else:
#         return s  
#     # Return original if length is not a multiple of 4

# # Get input from the user
# user_input = input("Enter a string: ")

# # Call the function
# result = reverse_if_multiple_of_4(user_input)

# # Display the result
# print("Result:", result)
# ==========================================================================================
# = This code defines a function that reverses a string if its length is a multiple of 4.
# = It then takes user input, calls the function, and prints the result.
# ==========================================================================================
# ==========================================================================================
# ==========================================================================================

# This code ignores the space between the words while counting and fimnding out 
# the length of the string, if multipler of 4 then it reverses the string and keep the spaces intact.
# ==========================================================================================
# ===========================================================================================

# This code defines a function that reverses a string if the number of letters (excluding spaces) is a multiple of 4.

def reverse_if_letters_multiple_of_4(s):
    # Remove only spaces for length check
    cleaned = s.replace(" ", "")
    
    if len(cleaned) % 4 == 0:
        return s[::-1]  # Reverse entire string including spaces
    else:
        return s
# Return original if length is not a multiple of 4
# Get input from the user
user_input = input("Enter a string: ")

# Call the function
result = reverse_if_letters_multiple_of_4(user_input)

# Display the result
print("Result:", result)
# Now if user input is example: Jay (Jay then Space) before it was counting the last space as
# part of the string and reversing it, now it will not count the space and reverse the string
# and keep the space intact.