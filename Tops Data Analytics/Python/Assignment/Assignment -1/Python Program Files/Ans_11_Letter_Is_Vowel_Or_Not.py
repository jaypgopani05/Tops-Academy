# Get input from the user
User_letter1 = input("Enter a single alphabet letter: ")

# Validate input
if len(User_letter1) != 1 or not User_letter1.isalpha():
    print("Invalid input! Please enter a single alphabet letter only.")
else:
    # Convert to lowercase for consistent checking
    letter = User_letter1.lower()
    # Keep the else part of process in background to hide from user. If you want to see the process, 
    # you can change the print statement to show the letter being checked.
    # 'a', 'e', 'i', 'o', 'u'.

    # Check if letter is a vowel or not.
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(f"{User_letter1} is a vowel.")
    else:
        print(f"{User_letter1} is not a vowel.")
# This program checks if the input letter is a vowel or not.
# It validates the input to ensure it's a single alphabet letter and then checks against the vowels '