# Get input from the user
sentence = input("Enter a sentence: ")

# Convert sentence to lowercase (optional for case-insensitive count)
sentence = sentence.lower()

# Split sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count the frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word frequencies
print("Word Frequency:")
for word, count in word_count.items():
    print(f"'{word}': {count}")
