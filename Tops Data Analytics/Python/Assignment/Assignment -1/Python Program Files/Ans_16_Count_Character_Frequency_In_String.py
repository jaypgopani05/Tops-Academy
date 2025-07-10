# Get input from the user
text = input("Enter a string: ")

# Create an empty dictionary to store character frequency
char_freq = {}

# Loop through each character in the string
for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Display the frequency of each character
print("Character Frequency:")
for char, count in char_freq.items():
    print(f"'{char}': {count}")
# Note: This code counts the frequency of each character in the string, including spaces and punctuation.
# The program consider upper case and lower case characters as different characters.
# If we want to ignore case, we can convert the string to lower case using text.lower