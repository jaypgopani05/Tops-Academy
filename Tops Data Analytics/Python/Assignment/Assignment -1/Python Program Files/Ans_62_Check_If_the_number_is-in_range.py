# # Define a function that checks whether a number is in a given range
# def check_in_range(num, start, end):
#     # Return True if number is between start and end (inclusive)
#     return start <= num <= end

# # Take user input with validation
# while True:
#     try:
#         # Ask the user for a number to check
#         number = int(input("Enter the number to check: "))

#         # Ask the user for the start of the range
#         range_start = int(input("Enter the start of the range: "))

#         # Ask the user for the end of the range
#         range_end = int(input("Enter the end of the range: "))

#         # Break out of loop if all inputs are valid
#         break
#     except ValueError:
#         # Handle invalid input (non-integer)
#         print("❌ Please enter valid integer values only.")

# # Call the function to check if number is in range
# if check_in_range(number, range_start, range_end):
#     print(f"✅ Yes, {number} is in the range [{range_start}, {range_end}].")
# else:
#     print(f"❌ No, {number} is NOT in the range [{range_start}, {range_end}].")



# ------------------------------------------------------------------------------------------------------------------------------------
# output:

# Part-1:
# Enter the number to check: 30
# Enter the start of the range: 100
# Enter the end of the range: -200
# ❌ No, 30 is NOT in the range [100, -200].

# Part-2:
# Enter the number to check: 10
# Enter the start of the range: -100
# Enter the end of the range: 30
# ✅ Yes, 10 is in the range [-100, 30].
# -------------------------------------------------------------------------------------------------------------------------------------
# Updated program as below:
# Handle the revrse ranging as well.
# e.g. range :  [-200 <- 30 <- 100] and [100 -> 30 -> -200]
# -------------------------------------------------------------------------------------------------------------------------------------

def check_in_range(num, start, end):
    # Normalize the range so it always goes from smaller to larger
    lower = min(start, end)
    upper = max(start, end)
    return lower <= num <= upper

# Take user input with validation
while True:
    try:
        number = int(input("Enter the number to check: "))
        range_start = int(input("Enter the start of the range: "))
        range_end = int(input("Enter the end of the range: "))
        break
    except ValueError:
        print("❌ Please enter valid integer values only.")

# Call the function
if check_in_range(number, range_start, range_end):
    print(f"✅ Yes, {number} is in the range [{min(range_start, range_end)}, {max(range_start, range_end)}].")
else:
    print(f"❌ No, {number} is NOT in the range [{min(range_start, range_end)}, {max(range_start, range_end)}].")
