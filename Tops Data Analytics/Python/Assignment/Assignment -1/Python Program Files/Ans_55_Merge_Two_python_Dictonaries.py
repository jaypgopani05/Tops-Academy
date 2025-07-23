# # Create the first dictionary with some key-value pairs
# dict1 = {'a': 1, 'b': 2, 'c': 3}

# # Create the second dictionary with some other key-value pairs
# dict2 = {'d': 4, 'e': 5, 'f': 6}

# # Create a new empty dictionary to store the merged result
# merged_dict = {}

# # Add all items from the first dictionary to the merged dictionary
# for key in dict1:
#     merged_dict[key] = dict1[key]

# # Add all items from the second dictionary to the merged dictionary
# for key in dict2:
#     merged_dict[key] = dict2[key]

# # Print the final merged dictionary
# print("Merged dictionary:")
# print(merged_dict)

# ----------------------------------------------------------------------------------------------------------------------------
#  Taking User Input and rewritting the code
# ----------------------------------------------------------------------------------------------------------------------------

# Create empty dictionaries for user input
dict1 = {}
dict2 = {}

# Ask the user how many items to enter for the first dictionary
count1 = int(input("Enter number of items in the first dictionary: "))

# Get key-value pairs from the user for the first dictionary
print("\nEnter items for first dictionary:")
for i in range(count1):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for key '{key}': ")
    
    # If the key already exists, append to the list
    if key in dict1:
        dict1[key].append(value)
    else:
        dict1[key] = [value]

# Ask the user how many items to enter for the second dictionary
count2 = int(input("\nEnter number of items in the second dictionary: "))

# Get key-value pairs from the user for the second dictionary
print("\nEnter items for second dictionary:")
for i in range(count2):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for key '{key}': ")
    
    # If the key already exists, append to the list
    if key in dict2:
        dict2[key].append(value)
    else:
        dict2[key] = [value]

# Merge both dictionaries into a new one
merged_dict = {}

# Add items from dict1 to merged_dict
for key in dict1:
    merged_dict[key] = dict1[key]

# Add items from dict2 to merged_dict
for key in dict2:
    if key in merged_dict:
        merged_dict[key].extend(dict2[key])  # Merge the lists
    else:
        merged_dict[key] = dict2[key]

# Print the final merged dictionary
print("\nMerged dictionary:")
print(merged_dict)
