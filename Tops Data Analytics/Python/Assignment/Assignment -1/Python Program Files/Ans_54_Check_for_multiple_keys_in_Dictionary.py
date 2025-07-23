# Create a sample dictionary with some key-value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Ask the user to input the keys they want to check
# User can separate keys with comma or space
keys_input = input("\nEnter keys to check (separated by comma or space): ")

# Replace any commas with spaces, then split the string into a list of keys
keys = keys_input.replace(',', ' ').split()

# Create two empty lists to store found and missing keys
found_keys = []       # This will hold keys that exist in the dictionary
missing_keys = []     # This will hold keys that are not in the dictionary

# Loop through each key entered by the user
for key in keys:
    # Check if the key is present in the dictionary
    if key in my_dict:
        # If key is found, add it to the found_keys list
        found_keys.append(key)
    else:
        # If key is not found, add it to the missing_keys list
        missing_keys.append(key)
        # Also print the missing key
        print("Key not found:", key)

# After checking all keys, decide what to show
if len(missing_keys) == 0:
    # If no keys are missing, print success message
    print("✅ All keys exist in the dictionary.")
else:
    # If some keys are missing, print a warning
    print("\n❌ Some keys are missing.")
    
    # Print a line separator for better formatting
    print("\n" + "-" * 90)
    
    # Print the list of keys that were found in the dictionary
    print("\nThe list of found keys are:", found_keys)
    
    # Print the list of keys that were not found in the dictionary
    print("\nThe list of missing keys are:", missing_keys)
    
    # Print another line separator
    print("\n" + "-" * 90)
