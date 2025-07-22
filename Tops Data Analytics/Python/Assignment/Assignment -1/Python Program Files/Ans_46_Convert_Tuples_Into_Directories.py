def get_tuples_for_dict():
    # Ask user how many key-value pairs to input
    while True:
        try:
            n = int(input("How many pairs do you want to enter? "))
            if n < 1:
                print("⚠️ Please enter at least one pair.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    tuple_list = []
    
    for i in range(n):
        while True:
            user_input = input(f"Enter key and value for pair #{i+1} (e.g., name,Jay): ")
            parts = [p.strip() for p in user_input.split(',')]
            if len(parts) != 2:
                print("⚠️ Please enter exactly one key and one value separated by a comma.")
                continue
            key, value = parts
            tuple_list.append((key, value))
            break

    return tuple_list

# Main Program
print("🔄 Convert a List of Tuples into a Dictionary")

# Get list of tuples from user
tuple_data = get_tuples_for_dict()

# Display list of tuples
print("\nList of tuples:", tuple_data)

# Convert to dictionary
converted_dict = dict(tuple_data)

# Display dictionary
print("Dictionary:", converted_dict)
