# Sample string given
sample_str = 'w3resource'

# Create an empty dictionary to store letter counts
letter_count = {}

# Loop through each character in the string
for char in sample_str:
    # If character already exists in dictionary, increment its count
    if char in letter_count:
        letter_count[char] += 1
    else:
        # If character is new, initialize count as 1
        letter_count[char] = 1

# Print the resulting dictionary
print("✅ Character frequency in the string:")
print(letter_count)
