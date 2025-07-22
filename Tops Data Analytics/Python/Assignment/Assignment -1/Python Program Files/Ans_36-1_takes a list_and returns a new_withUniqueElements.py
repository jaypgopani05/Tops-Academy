# Define a function to get unique elements from a list
def get_unique_elements(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    
    # Loop through each item in the input list
    for item in input_list:
        # Check if the item is not already in the unique_list
        if item not in unique_list:
            # If it's not, add it to unique_list
            unique_list.append(item)
    
    # Return the list with unique elements
    return unique_list

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5]  # Original list with duplicates
result = get_unique_elements(original_list)  # Call the function and store result

# Print the original and unique list
print("Original list:", original_list)       # Output the original list
print("Unique elements:", result)            # Output the list with unique values
