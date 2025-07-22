# Function to remove duplicates from a list while preserving order
# def remove_duplicates(original_list):
#     unique_list = []
#     for item in original_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list


# # --- Step 1: Get user input ---
# user_input = input("Enter numbers separated by space or comma:\n")

# # --- Step 2: Convert input string to a list of numbers ---
# # Replace commas with spaces, then split by space
# raw_items = user_input.replace(",", " ").split()

# # Try to convert all items to integers, ignore invalid entries
# cleaned_data = []
# for item in raw_items:
#     try:
#         num = int(item)
#         cleaned_data.append(num)
#     except ValueError:
#         print(f"😒 Skipping invalid entry: '{item}'")

# # --- Step 3: Remove duplicates ---
# unique_data = remove_duplicates(cleaned_data)

# # --- Step 4: Display Results ---
# print("\n😮 Original input count :", len(cleaned_data))
# print("🤷‍♂️ Unique values count   :", len(unique_data))
# print("😎 Duplicates removed    :", len(cleaned_data) - len(unique_data))

# # --- Step 5: Display the cleaned list in rows of 10 numbers ---
# print("\n🐐 Unique List Values:")
# for i in range(0, len(unique_data), 10):  # Every 10 items per line
#     row = unique_data[i:i+10]
#     print("  ", "  ".join(str(x).rjust(3) for x in row))
# --- end of code ---
# This code removes duplicates from a user-input list of numbers while preserving the order of first occurrences.
# It also handles invalid entries gracefully and displays the results in a formatted manner.
# This code is designed to be user-friendly and informative, providing clear feedback on the input process.
# Working with lists and user input in Python can be straightforward with the right approach.
# Now this code is ready to be executed in a Python environment.
# ===================================================================================================================================
# ===================================================================================================================================
# Need to handle all garbage inputs and remove duplicates from the user input list.
# Valoidating input with data types and handle the garbage value in out put and restricting it to listed as unique values.
# 
# ===================================================================================================================================
# ===================================================================================================================================

# Function to remove duplicates while preserving order
# def remove_duplicates(original_list):
#     unique_list = []
#     for item in original_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

# # Function to find duplicates in a list
# def find_duplicates(original_list):
#     seen = []
#     duplicates = []
#     for item in original_list:
#         if item in seen and item not in duplicates:
#             duplicates.append(item)
#         else:
#             seen.append(item)
#     return duplicates

# # --- Step 1: Get user input ---
# print("Enter values (numbers, words, etc.) separated by space or comma:")
# user_input = input()

# # --- Step 2: Manually split input on comma or space ---
# raw_items = []
# current = ""
# for char in user_input:
#     if char == ',' or char == ' ':
#         if current != "":
#             raw_items.append(current)
#             current = ""
#     else:
#         current += char
# if current != "":
#     raw_items.append(current)

# # --- Step 3: Validate and categorize entries ---
# valid_entries = []

# for item in raw_items:
#     val = item.strip()

#     if val == "":
#         continue

#     # Integer check
#     if val.isdigit():
#         valid_entries.append(int(val))
#         continue

#     # Float check (only one dot, all other chars digits)
#     dot_count = 0
#     valid_float = True
#     for ch in val:
#         if ch == '.':
#             dot_count += 1
#         elif not ch.isdigit():
#             valid_float = False
#             break

#     if valid_float and dot_count == 1:
#         try:
#             valid_entries.append(float(val))
#             continue
#         except:
#             pass

#     # Alphanumeric or alphabetic string
#     if val.isalpha() or val.isalnum():
#         valid_entries.append(val)
#         continue

#     # Invalid
#     print(f"😒 Skipping invalid entry: '{val}'")

# # --- Step 4: Find unique and duplicate values ---
# unique_values = remove_duplicates(valid_entries)
# duplicate_values = find_duplicates(valid_entries)

# # --- Step 5: Count data types ---
# int_count = 0
# float_count = 0
# string_count = 0

# for val in unique_values:
#     if type(val) == int:
#         int_count += 1
#     elif type(val) == float:
#         float_count += 1
#     elif type(val) == str:
#         string_count += 1

# # --- Step 6: Display results ---

# print("\n😮 Total valid entries      :", len(valid_entries))
# print("✅ Unique values count       :", len(unique_values))
# print("❌ Duplicate values count    :", len(duplicate_values))
# print(f"🔢 Integers: {int_count}, 🔣 Floats: {float_count}, 🔤 Strings: {string_count}")

# print("\n✅ Unique Values:")
# for i in range(0, len(unique_values), 10):
#     row = unique_values[i:i+10]
#     print("  ", "  ".join(str(x).rjust(6) for x in row))

# print("\n❌ Duplicate Values:")
# if duplicate_values:
#     for i in range(0, len(duplicate_values), 10):
#         row = duplicate_values[i:i+10]
#         print("  ", "  ".join(str(x).rjust(6) for x in row))
# else:
#     print("  None 👌")
# This code is designed to handle user input, validate it, remove duplicates, and display the results in a user-friendly manner.
# It includes functionality to categorize entries by type and handle invalid inputs gracefully.
# The code is structured to be clear and maintainable, with functions for specific tasks.
# It is ready to be executed in a Python environment and can be adapted for various input scenarios.
# ===================================================================================================================================
# ===================================================================================================================================

# Still this code is not handling any garbage value from user input and removing duplicates from the user input list.
# Need to refine garbage values from user input only ex:- abc.12, 12.1.12, abc.bc.b,@?GH!2 etc.
# also allow code to find duplicate and remove and list unique values from the user input list.
# ===================================================================================================================================
# ===================================================================================================================================

# # Function to remove duplicates while preserving order
# def remove_duplicates(original_list):
#     unique_list = []
#     for item in original_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

# # Function to find duplicates in a list
# def find_duplicates(original_list):
#     seen = []
#     duplicates = []
#     for item in original_list:
#         if item in seen and item not in duplicates:
#             duplicates.append(item)
#         else:
#             seen.append(item)
#     return duplicates

# # --- Step 1: Get user input ---
# print("Enter values (numbers, words, etc.) separated by space or comma:")
# user_input = input()

# # --- Step 2: Manually split input on comma or space ---
# raw_items = []
# current = ""
# for char in user_input:
#     if char == ',' or char == ' ':
#         if current != "":
#             raw_items.append(current)
#             current = ""
#     else:
#         current += char
# if current != "":
#     raw_items.append(current)

# # --- Step 3: Validate and categorize entries ---
# valid_entries = []

# for item in raw_items:
#     val = item.strip()

#     if val == "":
#         continue

#     # Integer check
#     if val.isdigit():
#         valid_entries.append(int(val))
#         continue

#     # Float check (only one dot, all other chars digits)
#     dot_count = 0
#     valid_float = True
#     for ch in val:
#         if ch == '.':
#             dot_count += 1
#         elif not ch.isdigit():
#             valid_float = False
#             break

#     if valid_float and dot_count == 1:
#         try:
#             valid_entries.append(float(val))
#             continue
#         except:
#             pass

#     # Alphanumeric or alphabetic string
#     if val.isalpha() or val.isalnum():
#         valid_entries.append(val)
#         continue

#     # Invalid
#     print(f"😒 Skipping invalid entry: '{val}'")

# # --- Step 4: Find unique and duplicate values ---
# unique_values = remove_duplicates(valid_entries)
# duplicate_values = find_duplicates(valid_entries)

# # --- Step 5: Count data types ---
# int_count = 0
# float_count = 0
# string_count = 0

# for val in unique_values:
#     if type(val) == int:
#         int_count += 1
#     elif type(val) == float:
#         float_count += 1
#     elif type(val) == str:
#         string_count += 1

# # --- Step 6: Display results ---

# print("\n😮 Total valid entries      :", len(valid_entries))
# print("✅ Unique values count       :", len(unique_values))
# print("❌ Duplicate values count    :", len(duplicate_values))
# print(f"🔢 Integers: {int_count}, 🔣 Floats: {float_count}, 🔤 Strings: {string_count}")

# print("\n✅ Unique Values:")
# for i in range(0, len(unique_values), 10):
#     row = unique_values[i:i+10]
#     print("  ", "  ".join(str(x).rjust(6) for x in row))

# print("\n❌ Duplicate Values:")
# if duplicate_values:
#     for i in range(0, len(duplicate_values), 10):
#         row = duplicate_values[i:i+10]
#         print("  ", "  ".join(str(x).rjust(6) for x in row))
# else:
#     print("  None 👌")

# ====================================================================================================================================
# ====================================================================================================================================

# going infinite loop-- after one execution it is running again automatic. need to fix it.
# Still output is not as expected!!!
# ====================================================================================================================================
# ====================================================================================================================================

import re

# ✅ Remove duplicates (preserves order)
def remove_duplicates(data):
    unique = []
    for item in data:
        if item not in unique:
            unique.append(item)
    return unique

# ✅ Find duplicates (preserves order)
def find_duplicates(data):
    seen = []
    duplicates = []
    for item in data:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.append(item)
    return duplicates

# ✅ Get input from user
print("📥 Enter values separated by space or comma (words, numbers, names etc.):")
user_input = input().strip()

# ✅ Split on space or comma
raw_items = re.split(r'[,\s]+', user_input)

valid_entries = []
garbage_entries = []

for val in raw_items:
    val = val.strip()
    if not val:
        continue

    # ✅ Check integer
    if val.isdigit():
        valid_entries.append(int(val))
        continue

    # ✅ Check float (1 dot only, numeric on both sides)
    if val.count('.') == 1:
        left, right = val.split('.')
        if left.replace('-', '').isdigit() and right.isdigit():
            valid_entries.append(float(val))
            continue

    # ✅ Check strings: alphabetic or alphanumeric (no symbols)
    if val.isalnum():
        valid_entries.append(val)
        continue

    # ❌ Garbage
    garbage_entries.append(val)

# ✅ Process results
unique_values = remove_duplicates(valid_entries)
duplicate_values = find_duplicates(valid_entries)

# ✅ Type counts
int_count = sum(isinstance(x, int) for x in unique_values)
float_count = sum(isinstance(x, float) for x in unique_values)
str_count = sum(isinstance(x, str) for x in unique_values)

# ✅ Output Summary
print("\n🔍 Summary:")
print("😮 Total valid entries      :", len(valid_entries))
print("✅ Unique values count       :", len(unique_values))
print("❌ Duplicate values count    :", len(duplicate_values))
print(f"🔢 Integers: {int_count}, 🔣 Floats: {float_count}, 🔤 Strings: {str_count}")
print("🚫 Garbage values removed   :", len(garbage_entries))

# ✅ Display Unique Values
print("\n🐐 Unique List Values:")
for i in range(0, len(unique_values), 10):
    row = unique_values[i:i+10]
    print("  ", "  ".join(str(x).rjust(4) for x in row))

# ✅ Display Duplicates
print("\n❌ Duplicate Values:")
if duplicate_values:
    for i in range(0, len(duplicate_values), 10):
        row = duplicate_values[i:i+10]
        print("  ", "  ".join(str(x).rjust(4) for x in row))
else:
    print("  None 👌")

# ✅ Display Garbage
print("\n🗑️ Garbage (Invalid) Entries:")
if garbage_entries:
    for i in range(0, len(garbage_entries), 10):
        row = garbage_entries[i:i+10]
        print("  ", "  ".join(str(x).rjust(6) for x in row))
else:
    print("  None 👌")

# ✅ End
print("\n🎉 Program finished. Exiting...")
# Now Its Working Fine
# --- end of code ---
# ==================================================================================================================================
# ==================================================================================================================================