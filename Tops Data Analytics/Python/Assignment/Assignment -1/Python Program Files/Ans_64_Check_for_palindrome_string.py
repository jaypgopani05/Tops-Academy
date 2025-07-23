# Function to check if a given string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniform comparison
    s = s.replace(" ", "").lower()

    # Compare the string with its reverse
    return s == s[::-1]

# -------- Main Program --------

# Take string input from user
user_input = input("Enter a string to check if it's a palindrome: ")

# Call the function and print result
if is_palindrome(user_input):
    print(f"✅ Yes, '{user_input}' is a Palindrome.")
else:
    print(f"❌ No, '{user_input}' is NOT a Palindrome.")

# Note: A string that reads same from front and back called palindrome.
