# Define a function to convert list of characters into a string
def convert_list_to_string(char_list):
    # Use join() to concatenate all characters into one string
    result = ''.join(char_list)
    return result

# Example list of characters
char_list = ['H', 'e', 'l', 'l', 'o', ' ', 'J', 'a', 'y']

# Call the function and store the result
final_string = convert_list_to_string(char_list)

# Print the output
print("List of characters:", char_list)
print("Converted string:", final_string)
#  Note:
# Taking user input in part 2.
# Managing space or separating words issues after taking user input.
# Include real time space as well.