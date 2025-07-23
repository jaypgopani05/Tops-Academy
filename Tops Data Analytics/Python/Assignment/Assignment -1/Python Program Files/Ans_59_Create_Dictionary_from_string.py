# Ask the user to enter a string
user_input = input("Enter a string: ")

# Create an empty dictionary to store the count of each character
letter_count = {}

# Loop through each character in the input string
for char in user_input:
    # Skip spaces so they are not counted
    if char == " ":
        continue

    # If the character is already in the dictionary, increase its count
    if char in letter_count:
        letter_count[char] += 1
    else:
        # If character is not in dictionary, add it with count 1
        letter_count[char] = 1

# Print the final dictionary showing letter counts
print("\n✅ Letter count from the string:")
print(letter_count)
