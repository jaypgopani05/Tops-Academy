def get_unique_elements(input_list):
    # Create a list to store only unique values
    unique_list = []
    for item in input_list:
        # Add item only if not already in unique_list
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

try:
    # Ask user for input
    user_input = input("Enter elements separated by commas or spaces (e.g., 1,2,3 or apple banana apple): ")

    # Choose delimiter based on input
    if "," in user_input:
        raw_list = user_input.split(",")  # Split by comma
    else:
        raw_list = user_input.split()     # Split by spaces

    # Strip whitespace and filter out empty strings
    cleaned_list = [item.strip() for item in raw_list if item.strip() != ""]

    # Validate input
    if not cleaned_list:
        raise ValueError("Input list is empty or invalid.")

    # Get unique elements
    result = get_unique_elements(cleaned_list)

    # Show results
    print("Original list:", cleaned_list)
    print("Unique elements:", result)

except Exception as e:
    print("Error:", e)
#  --- End of Code ---
# This python program is working fine and showing accurate results.
# The string "jay" and "jay" will be considered as two different unique values. 
# If we need to change it we just need to change the for loop in the starting part and declare as follows:

# seen_lower = set()                            # Track items in lowercase for comparison
    # for item in input_list:
    #     if item.lower() not in seen_lower:
    #         unique_list.append(item)          # Keep original case
    #         seen_lower.add(item.lower())      # Track lowercase version
    # return unique_list