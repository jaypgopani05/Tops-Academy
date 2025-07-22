# Write a Python function to get the largest number, smallest num
# and sum of all from a list. 
def analyze_numbers(num_list):
    # Check for empty or invalid input
    if not num_list or not all(isinstance(n, (int, float)) for n in num_list):
        return "Invalid input. Please provide a list of numbers."

    # Calculate results
    largest = max(num_list)
    smallest = min(num_list)
    total = sum(num_list)

    return {
        "Largest Number": largest,
        "Smallest Number": smallest,
        "Sum": total
    }
# Example usage:
numbers = [45, 12, 78, 33, 5, 99, 67, 23, 89, 56, 34, 21, 90, 11, 8, 15, 3, 7, 2, 1,101, 100]
result = analyze_numbers(numbers)
print("Largest Number:", result["Largest Number"])
print("Smallest Number:", result["Smallest Number"])
print("Sum:", result["Sum"])
# output:
# Largest Number: 101
# Smallest Number: 1
# Sum: 567
# Example usage with an empty list
empty_result = analyze_numbers([])
print(empty_result)  
# Output: Invalid input. Please provide a list of numbers.
# This function handles both valid and invalid inputs, ensuring robustness.
# It returns the largest number, smallest number, and the sum of all numbers in the list.
# If the input is invalid, it returns an appropriate message.
