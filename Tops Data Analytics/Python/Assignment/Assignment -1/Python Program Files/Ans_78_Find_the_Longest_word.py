# 78) Write a Python program to find the longest word(s) from a user input.

# Step 1: Take a string input from the user
user_input = input("Enter a sentence or list of words: ")

# Step 2: Split the input string into words using space as the delimiter
words = user_input.split()

# Step 3: Initialize a variable to keep track of the longest word
longest_word = ""

# Step 4: Loop through each word in the list of words
for word in words:
    # Step 5: If the current word is longer than the longest_word found so far
    if len(word) > len(longest_word):
        longest_word = word  # Update longest_word to the current word

# Step 6: Print the longest word found
print(f"The longest word is: {longest_word}")
# ==================================================================================================================================
# ==================================================================================================================================
# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_78_Find_the_Longest_word.py"
# Enter a sentence or list of words: Jay Gopani Piyushkumar Tops Technologies Ambavadi Ahmedabad Gujarat India
# The longest word is: Technologies
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 

# ===================================================================================================================================
# ===================================================================================================================================