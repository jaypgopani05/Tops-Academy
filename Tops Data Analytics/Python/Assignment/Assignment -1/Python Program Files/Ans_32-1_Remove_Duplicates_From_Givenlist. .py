# Function to remove duplicates from a list while preserving the original order
def remove_duplicates(original_list):
    unique_list = []
    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


# --- Original Data (with duplicates) ---
data = [
    10, 20, 10, 30, 20, 40, 50, 30, 60, 50, 70, 80, 90, 80, 100, 100, 110, 120,
    130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270,
    280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420,
    430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570,
    580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700
]

# --- Remove duplicates using the function ---
unique_data = remove_duplicates(data)

# --- Output Summary ---
print("Original list length :", len(data))                     # Total items in original list
print("Unique list length   :", len(unique_data))              # Total items after duplicates removed
print("Duplicates removed   :", len(data) - len(unique_data))  # Number of duplicates removed

# --- Display the cleaned list in rows of 10 elements each ---
print("\nUnique List Values:")
for i in range(0, len(unique_data), 10):  # Loop over every 10 items
    row = unique_data[i:i+10]            # Slice 10 items per row
    print("  ", "  ".join(str(x).rjust(3) for x in row))  # Format numbers with right alignment
# --- End of Code ---
# This code removes duplicates from a given list while preserving the order of elements. 
# It prints the original list length, the unique list length, and the number of duplicates removed.
# It also displays the unique values in rows of 10 elements each, formatted for better readability.
# This approach ensures that the original order of elements is maintained while efficiently removing duplicates.
# This code is useful for data cleaning tasks where maintaining the order of elements is important, 
# such as in data preprocessing for machine learning or data analysis.
# The function `remove_duplicates` iterates through the original list and appends only unique items to a new list.
# # The output is formatted to show the unique values in a structured manner, making it easy to read and analyze.
# # The code is designed to be simple and efficient, suitable for small to medium-sized lists.
# # The code can be easily modified to handle larger datasets or different data types if needed.
# # The code is written in Python and can be executed in any Python environment.
# # The code is self-contained and does not require any external libraries or dependencies.
# Now let's try to take input list from user and formate the output along with validating inputs.