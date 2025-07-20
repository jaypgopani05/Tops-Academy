# # Get input from the user
# sentence = input("Enter a sentence: ")

# # Convert sentence to lowercase (optional for case-insensitive count)
# sentence = sentence.lower()

# # Split sentence into words
# words = sentence.split()

# # Create an empty dictionary to store word counts
# word_count = {}

# # Count the frequency of each word
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# # Display the word frequencies
# print("Word Frequency:")
# for word, count in word_count.items():
#     print(f"'{word}': {count}")

# Need to improve the code to handle punctuation and special characters
# This can be done by using regex or string methods to clean the words before counting.
# For example, you can use `word.strip('.,!?;:')` to remove common punctuation marks.
# To improve the code further, we can use regex to handle punctuation and special characters

# =================================================================================================================
# =================================================================================================================

# Get input from the user
sentence = input("Enter a sentence: ")

# Convert to lowercase for case-insensitive counting
sentence = sentence.lower()

# Common punctuation marks to remove
punctuations = ".,!?;:-()[]{}\"*#@$%^&+=~`'"

# Split sentence into words
words = sentence.split()

# Clean punctuation from each word and count
word_count = {}

for word in words:
    # Strip punctuation from both ends of the word
    clean_word = word.strip(punctuations)
    
    # Skip empty strings if any
    if clean_word:
        if clean_word in word_count:
            word_count[clean_word] += 1
        else:
            word_count[clean_word] = 1

# Display the result
print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"'{word}': {count}")
# =================================================================================================================
# =================================================================================================================
# This code will now correctly count the frequency of words in a sentence while ignoring punctuation and case.
# It handles common punctuation marks and ensures that words are counted accurately.
# You can further enhance it by using regex for more complex punctuation handling if needed.
# For example, you could use `re.sub(r'[^\w\s]', '', word)` to remove all non-word characters.
# This would require importing the `re` module at the beginning of your script.