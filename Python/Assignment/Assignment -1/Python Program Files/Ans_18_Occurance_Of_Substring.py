# Get the main string and substring from the user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

# Use the count() method to find occurrences
count = main_string.count(substring)

# Display the result
print(f"The substring '{substring}' occurs {count} times in the string.")
# Note: This code is case-sensitive. If you want to perform a case-insensitive,
# We can convert both strings to lower case using .lower()
# or .upper() before counting.
# The program consider upper case and lower case characters as different characters.