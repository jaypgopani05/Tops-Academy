# Keep asking for a valid number of items until user provides a correct input
while True:
    num_input = input("Enter the number of items in the dictionary: ")
    if num_input.isdigit():
        n = int(num_input)
        break
    else:
        print("❌ Please enter a valid number (e.g. 2, 3, 4, 5)")

# Check if user entered at least 3 items
if n < 3:
    print("\n❗❗❗ Please enter more than 3 items in the dictionary to find")
    print("\ttop 3 values from the list of dictionary.\n")
    print("\t\b Please try again... \b")
    exit()

# Create an empty dictionary
my_dict = {}

# Take key-value pairs from user input
print("\nEnter key-value pairs (values must be numbers):")
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    
    # Keep asking for the value until a valid number is entered
    while True:
        value_input = input(f"Enter value for key '{key}': ")
        
        # Check if the entered value is a number (only digits allowed)
        if value_input.isdigit():
            value = int(value_input)
            break
        else:
            print("❌ Please enter a numeric value (e.g., 100, 200).")

    # Add key-value to dictionary
    my_dict[key] = value

# Sort the dictionary values in descending order
sorted_values = sorted(my_dict.values(), reverse=True)

# Get the top 3 values
top_3 = sorted_values[:3]

# Print the top 3 values
print("\nTop 3 highest values in the dictionary:")
print(top_3)
