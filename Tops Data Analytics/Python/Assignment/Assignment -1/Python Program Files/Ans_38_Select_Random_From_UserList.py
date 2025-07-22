# 38)Write a Python program to select an item randomly from a list. 
import random  # Import random module for selection

# Function to randomly select one item from the list
def pick_random_item(item_list):
    return random.choice(item_list)  # Select and return one random item

# Main program
try:
    # Ask for user input
    user_input = input("Enter items separated by commas or spaces (e.g., apple, banana, mango): ").strip()

    # Check if input is empty
    if not user_input:
        raise ValueError("Input cannot be empty. Please enter at least two items.")

    # Use regex to allow space or comma as separator
    import re
    raw_items = re.split(r'[,\s]+', user_input)

    # Clean the list: remove empty strings
    items = [item for item in raw_items if item]

    # Validate that at least 2 items are entered
    if len(items) < 2:
        raise ValueError("Please enter at least two valid items.")

    # Call function to pick a random item
    selected = pick_random_item(items)

    # Display result
    print("✅ Items List:", items)
    print("🎯 Randomly Selected Item:", selected)

except Exception as e:
    print("⚠️ Error:", e)