# Get two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if both strings have at least 2 characters
if len(str1) < 2 or len(str2) < 2:
    print("Both strings must have at least 2 characters.")
else:
    # Swap the first two characters of each string
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    # Combine with a space in between
    result = new_str1 + " " + new_str2

    # Display the result
    print("Resulting string:", result)
# Note: This code assumes that the user will enter valid strings with at least 2 characters. 
# and Validates it.
# ==========================================================================================
# ==========================================================================================
# ==========================================================================================
# Another Way of Doing if you don not Swap.....
# # Get two input strings from the user
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")

# # Just concatenate the strings with a space (no swap)
# result = str1 + " " + str2

# # Display the result
# print("Resulting string:", result)
# # Note: This code simply concatenates the two strings with a space in between.
# # It does not swap any characters, as per your request.