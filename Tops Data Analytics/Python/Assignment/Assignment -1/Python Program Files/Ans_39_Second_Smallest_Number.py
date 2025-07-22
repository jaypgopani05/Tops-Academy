# Function to find the second smallest number in a list
def find_second_smallest(numbers):
    # Convert list to a set to remove duplicates and sort the unique numbers
    unique_numbers = sorted(set(numbers))
    
    # Check if there are at least 2 unique numbers
    if len(unique_numbers) < 2:
        raise ValueError("Need at least two unique numbers to find the second smallest.")
    
    return unique_numbers[1]  # Return second smallest

# Main program
try:
    # Get user input
    user_input = input("Enter numbers separated by commas or spaces (e.g., 5,3,7,1,2): ").strip()

    # Check for empty input
    if not user_input:
        raise ValueError("Input cannot be empty.")

    # Import regex to split by space or comma
    import re
    split_values = re.split(r'[,\s]+', user_input)

    # Convert input to list of integers
    numbers = []
    for val in split_values:
        if val != '':
            if val.lstrip('-').isdigit():  # handles negative numbers too
                numbers.append(int(val))
            else:
                raise ValueError(f"Invalid number: {val}")

    # Ensure at least two numbers are present
    if len(numbers) < 2:
        raise ValueError("Please enter at least two numbers.")

    # Call the function
    second_smallest = find_second_smallest(numbers)

    # Print result
    print("✅ List of numbers:", numbers)
    print("✅ Second smallest number is:", second_smallest)

except Exception as e:
    print("⚠️ Error:", e)