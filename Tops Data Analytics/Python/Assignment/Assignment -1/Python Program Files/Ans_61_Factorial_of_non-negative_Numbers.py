# Define a function to calculate factorial
def calculate_factorial(number):
    # Return 1 if number is 0 or 1 (by definition)
    if number == 0 or number == 1:
        return 1

    # Initialize result as 1
    result = 1

    # Multiply numbers from 2 to the given number
    for i in range(2, number + 1):
        result *= i

    # Return the final result
    return result

# Keep asking user until valid number is entered
while True:
    try:
        # Take input from the user
        num = int(input("Enter One non-negative integer at a time (max 100): "))

        # Check if the number is negative
        if num < 0:
            print("❗ Please enter One non-negative number at a time.")
        # Check if the number is too large
        elif num > 100:
            print("❗ Please enter One smaller number (100 or less) to avoid large calculations.")
        else:
            break  # Exit loop if number is valid
    except ValueError:
        # Handle case when input is not an integer
        print("❌ Invalid input! Please enter One valid number (e.g., 5, 10).")

# Calculate factorial using the function and print it
print(f"✅ Factorial of {num} is: {calculate_factorial(num)}")
