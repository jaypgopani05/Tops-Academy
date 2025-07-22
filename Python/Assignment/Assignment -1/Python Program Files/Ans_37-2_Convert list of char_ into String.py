# Function to convert a list of characters into a single string
def convert_list_to_string(char_list):
    return ''.join(char_list)  # Join all characters into one string

# Main program
try:
    # Instructions for the user
    print("Note:")
    print("- Use commas `,` or spaces to separate characters.")
    print("- To include a real space between words, type an underscore `_`.")

    # Get user input
    user_input = input("Enter characters (e.g., H e l l o or J,a,y,_,G,o): ").strip()

    # Check if input is empty
    if not user_input:
        raise ValueError("❌ Input cannot be empty. Please enter some characters.")

    # Import regex module to split by commas or spaces
    import re
    raw_list = re.split(r'[,\s]+', user_input)

    # Process input: replace "_" with space and ignore empty strings
    char_list = []
    for char in raw_list:
        if char == '_':
            char_list.append(' ')  # underscore becomes space
        elif char != '':  # skip blanks
            char_list.append(char)

    # Check if at least two characters are entered
    if len(char_list) < 2:
        raise ValueError("❌ Please enter at least two characters.")

    # Validate: every element must be a single character
    for c in char_list:
        if len(c) != 1:
            raise ValueError(f"❌ '{c}' is not a single character.")

    # Convert to string
    final_string = convert_list_to_string(char_list)

    # Show output
    print("✅ List of characters:", char_list)
    print("✅ Converted string:", final_string)

except Exception as e:
    print("⚠️ Error:", e)
