# 31) Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list
# of strings

# def count_strings_with_same_first_last_char(strings):
#     count = 0
#     for s in strings:
#         if len(s) >= 2 and s[0] == s[-1]:
#             count += 1
#     return count
# =================================================================================================================
# This program is logically fine but need to insert the strings list from user to test the function. 
# ==================================================================================================================
# ==================================================================================================================

# # Test input list (you can add more examples)
# test_inputs = [
#     "wow hello bob Anna civic dog deed",
#     "apple banana",
#     "a,a aa bb cc dd d",
#     "noon moon mom madam kayak racecar",
#     "hey,yay,hey"
# ]

# # Loop through test inputs
# for user_input in test_inputs:
#     print(f"\n📥 Test Input: {user_input}")

#     # Replace commas with spaces to handle both separators, then split into a list
#     words = user_input.replace(',', ' ').split()

#     # Initialize a counter for valid words
#     count = 0

#     # Create a list to store matching words
#     matching_words = []

#     # Go through each word in the list
#     for word in words:
#         word = word.strip()  # Remove extra spaces
#         # Check if the word has at least 2 characters and the first and last characters are the same (case-insensitive)
#         if len(word) >= 2 and word[0].lower() == word[-1].lower():
#             count += 1  # Increase the count
#             matching_words.append(word)  # Add the word to the matching list

#     # Print the result
#     print("\n✅ Total matching words:", count)

#     # Print the words that matched the condition
#     if matching_words:
#         print("🟢 Words with same first and last character:")
#         for w in matching_words:
#             print("-", w)
#     else:
#         print("⚠️ No matching words found.")
#     print("-" * 50)


# ==================================================================================================================================

# Notes:-

# This program works fine but need to validate:
# The user input for empty input: 
# string input and numbers input both: 
# 
# Matching string output from user input should looks as below:
# ----- Result Summary -----
# Matching Strings from input (Alphabetic and Alphanumeric):

# Duplicates integer in Input:

# Total matching counts (including string and integers)

# Also need to handle the upper case and lower case input. Convert all input to lower case and then print the output as user printed.

# ==============================================================================================================================
# ==============================================================================================================================

# Predefined test inputs
test_inputs = [
    "Jay 123 jay 123", 
    "Anna 456 456.0 wow Bob bob", 
    "Tops 99 99 100 101 100", 
    "level noon noon 808", 
    "",  # Empty input test
]

# Loop through each test input
for user_input in test_inputs:
    print(f"\n📥 Test Input: {user_input}")

    # Validate empty input
    if not user_input.strip():
        print("❌ Error: No input provided.")
        print("-" * 50)
        continue

    # Replace commas with spaces, then split by space
    items = user_input.replace(',', ' ').split()

    # Remove extra spaces or empty entries
    items = [item.strip() for item in items if item.strip()]

    # Sets to store unique matches
    matching_strings = set()
    numeric_seen = set()
    numeric_duplicates = set()

    # Temporary set for checking string matches by lowercase
    matched_string_check = set()

    # Process each item
    for val in items:
        val_stripped = val.strip()

        # Check for strings that start and end with same character (case-insensitive)
        if val_stripped.isalnum() and len(val_stripped) >= 2:
            val_lower = val_stripped.lower()
            if val_lower[0] == val_lower[-1] and val_lower not in matched_string_check:
                matching_strings.add(val_stripped)  # Store original string
                matched_string_check.add(val_lower)  # Avoid case-insensitive duplicates

        # Check for numeric duplicates
        try:
            num = float(val_stripped) if '.' in val_stripped else int(val_stripped)
            if num in numeric_seen:
                numeric_duplicates.add(num)
            else:
                numeric_seen.add(num)
        except ValueError:
            continue  # Skip if not a valid number

    # --- Output Section ---
    print("\n📊 --- Result Summary ---")

    # Matching Strings Output
    print("\n🔤 Matching Strings (Alphabetic/Alphanumeric):")
    if matching_strings:
        for s in sorted(matching_strings):
            print(" -", s)
    else:
        print(" None")

    # Duplicate Numbers Output
    print("\n🔢 Duplicate Numeric Values:")
    if numeric_duplicates:
        for n in sorted(numeric_duplicates):
            print(" -", n)
    else:
        print(" None")

    # Total Count
    total_matches = len(matching_strings) + len(numeric_duplicates)
    print(f"\n✅ Total Matching Count (Strings + Duplicates in Numbers): {total_matches}")
    print("-" * 50)

# --- End of code ---
# This program has the output accurately user friendly.
# Notes:
# Empty input validated.
# Lower case input conversion validated.
# Matching string input with all conditions satisfied.
# added numeric and alphanumeric value matching and finds duplicate entries as well.
# Output is well organized and user friendly.
