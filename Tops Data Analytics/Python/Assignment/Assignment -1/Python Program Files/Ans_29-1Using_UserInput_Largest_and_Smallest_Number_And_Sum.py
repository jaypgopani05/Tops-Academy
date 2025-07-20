# The code is designed to find the largest, smallest, and sum of numbers in a list.
# It uses built-in functions max(), min(), and sum() for efficiency.
# The input is taken as a string, split into individual numbers, and converted to integers.
# The function returns the largest, smallest, and total sum of the numbers.
# User input is handled to create a list of integers.
# The code is efficient and handles empty lists gracefully.
# ===================================================================================================================
# ===================================================================================================================

# def list_search(numbers):
#     if not numbers:
#         return "The list is empty."

#     largest = max(numbers)
#     smallest = min(numbers)
#     total = sum(numbers)

#     return largest, smallest, total

# =====================================================================================================================
# =====================================================================================================================

# user= input("Enter a list of numbers separated by spaces: ")
# largest, smallest, total = list_search([int(x) for x in user.split()])
# print(f"Largest, Smallest, and Sum of the numbers in the list are: {largest}, {smallest}, {total}")
# This could be the best logical function to perform the task.
# However there are some other ways to do this as well. without having anu issue.
# ex: need to check for empty list, or float vlaue etc. ----> Need to throw an error if found any wrong type of value.
# The code is efficient and handles empty lists gracefully. ----> Need to print an error massege if the list is empty.
# Need to redesign the code to handle some of the issues mentioned above.

# ==================================================================================================================
# ==================================================================================================================

def search_list(numbers):
    if not numbers:
        return "Error: The list is empty or not provided."

    # Filter out non-numeric values
    clear_list = []
    for item in numbers:
        try:
            num = float(item)  # Converts valid numbers (int/float/str)
            clear_list.append(num)
        except ValueError:
            continue  # Ignore non-numeric values like 'abc'

    if not clear_list:
        return "Error: No valid numeric data in the list."

    largest = max(clear_list)
    smallest = min(clear_list)
    total = sum(clear_list)

    return largest, smallest, total


# ---- User Input Section ----
user_input = input("Enter numbers separated by commas: ")

# Convert input string to a list
input_list = [x.strip() for x in user_input.split(",") if x.strip()]

# Analyze the list
result = search_list(input_list)

# Display result
if isinstance(result, tuple):
    largest, smallest, total = result
    print("\n----> Results:")
    print("Largest number:", largest)
    print("Smallest number:", smallest)
    print("Sum of all numbers:", total)
else:
    print("\n!", result)  # Show error message


# Still one more issue found, if user do not put coma, and add space then it will not work.
# To handle this, we can modify the input processing to split by spaces as well.
# This will ensure that the input is flexible and user-friendly.