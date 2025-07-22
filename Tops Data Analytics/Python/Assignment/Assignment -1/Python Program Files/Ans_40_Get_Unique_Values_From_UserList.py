# Function to extract unique values from the input list
def get_unique_values(input_list):
    return list(set(input_list))  # Use set to remove duplicates, then convert back to list

# Main program
try:
    # Ask the user to input values
    user_input = input("Enter items separated by commas or spaces (e.g., apple, banana, apple, mango): ").strip()

    # Check for empty input
    if not user_input:
        raise ValueError("Input cannot be empty. Please enter at least one item.")

    # Import regex to split input by comma or space
    import re
    raw_items = re.split(r'[,\s]+', user_input)

    # Clean the list by removing empty strings
    items = [item.strip() for item in raw_items if item.strip()]

    # Validate the input length
    if len(items) < 1:
        raise ValueError("Please enter at least one valid item.")

    # Get unique values
    unique_items = get_unique_values(items)

    # Show results
    print("✅ Original List:", items)
    print("✨ Unique Values:", unique_items)

except Exception as e:
    print("⚠️ Error:", e)
