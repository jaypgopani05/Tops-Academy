# def insert_in_middle(O_Str, N_insert):
#     middle_index = len(O_Str) // 2
#     return O_Str[:middle_index] + N_insert + O_Str[middle_index:]

# # Get input from the user
# original_string = input("Enter the original string: ")
# string_to_insert = input("Enter the string to insert: ")

# # Call the function with user input
# result = insert_in_middle(original_string, string_to_insert)

# # Show the result
# print("Result:", result)

# Visual output is little off-bit. we need to do something about space between the strings in the final output.
# Adjusting the output to ensure proper spacing.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Get user input
# Get user input for the original string and the string to insert

# original_Str1 = input("Enter the original string (can include spaces): ")
# New_insert_Str = input("Enter the string to insert: ")

# # Step 1: Find indexes of all non-space characters
# non_space_positions = []
# for i in range(len(original_Str1)):
#     if original_Str1[i] != ' ':
#         non_space_positions.append(i)

# # Step 2: Check if enough characters to insert into
# if len(non_space_positions) < 2:
#     print("Error: Not enough non-space characters to insert.")
# else:
#     # Step 3: Calculate middle based on non-space characters
#     mid_pos = len(non_space_positions) // 2
#     insert_index = non_space_positions[mid_pos]  # actual index in original string

#     # Step 4: Build final string
#     result = original_Str1[:insert_index] + New_insert_Str + original_Str1[insert_index:]

#     # Step 5: Show output
#     print("Result:", result)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# ==================================================================================================================================================

# Still not working as expected. Let's try a different approach.
# We also need to check the length of string to insert and ensure it does not break the original string's spacing.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Get user input
# original = input("Enter the original string (can include spaces): ")
# to_insert = input("Enter the string to insert: ")

# # Step 1: Identify positions of non-space characters
# non_space_positions = []
# for i in range(len(original)):
#     if original[i] != ' ':
#         non_space_positions.append(i)

# # Step 2: Validate minimum characters
# if len(non_space_positions) < 2:
#     print("Error: Not enough non-space characters to insert.")
# else:
#     # Step 3: Find the actual index for insertion
#     mid_pos = len(non_space_positions) // 2
#     insert_index = non_space_positions[mid_pos]  # index in original string

#     # Step 4: Insert into original string at calculated index
#     result = original[:insert_index] + to_insert + original[insert_index:]

#     # Step 5a: Normal output (Option 2)
#     print("\n Output (Natural Spacing):")
#     print("Result:", result)

#     # Step 5b: Visible spacing output (Option 3)
#     visible_result = ''
#     for ch in result:
#         if ch == ' ':
#             visible_result += '␣'  # visible space character
#         else:
#             visible_result += ch

#     print("\n Output (Spaces Shown Visibly):")
#     print("Result:", visible_result)


#  This code will show two different outputs:
# 1. The natural output with proper spacing.
# 2. The output with spaces shown visibly using a special character.
# Which basically solves the problem of showing spaces in the output.
# This approach ensures that the insertion is done correctly while maintaining the integrity of the original string's spacing.
# Uses only basic python (loops,slicing,string operations) without any advanced libraries.
# Fully handles the space counting rule.
# makes output more readable by showing spaces visibly and debug friendly.
# We can disable one of the output and keep the other one based on user preference.
# 
# 
# Still there is one more problem of showing the output. if any string is inserted in the middle of the string, it will not show the output properly.
# And does not add space automatically. ex: original string: Piyush Gopani , New String to Insert: D.
# FInal output will be:  Piyush D.Gopani . which is not correct. There should be auto space added after the inserted string. to have a clear visual output.
# need to work on auto spacing functions.

# =====================================================================================================================================================================
# =====================================================================================================================================================================
# =====================================================================================================================================================================

# Final Version Code
# Adding Auto Space After Insertion and before Insertion if needed.
# if auto_space:
#     result = original[:insert_index] + ' ' + to_insert.strip() + ' ' + original[insert_index:]
# else:
#     result = original[:insert_index] + to_insert + original[insert_index:]

# =================================================================================
# =================================================================================

# Get user input
original = input("Enter the original string (can include spaces): ")
New_insert = input("Enter the string to insert: ")

# Optional toggle: Enable or disable automatic spacing around the inserted string
auto_space = True

# Let's Identify positions of non-space characters in given original string
non_space_positions = []
for i in range(len(original)):
    if original[i] != ' ':
        non_space_positions.append(i)

# Now Validate enough non-space characters
if len(non_space_positions) < 2:
    print("Error: Not enough non-space characters to insert.")
else:
    # Do Find actual index in original string
    mid_pos = len(non_space_positions) // 2
    insert_index = non_space_positions[mid_pos]

    # Try to Build the result with or without auto spacing
    if auto_space:
        # Ensure single space before/after insert if not already present
        insert_clean = New_insert.strip()
        result = (
            original[:insert_index] +
            ' ' + insert_clean + ' ' +
            original[insert_index:]
        )
    else:
        result = original[:insert_index] + New_insert + original[insert_index:]

    # Finally, Normal output
    print("\n Output (Natural Spacing):")
    print("Result:", result)

    # And Output with visible space markers
    visible_result = ''
    for ch in result:
        if ch == ' ':
            visible_result += '_'  # You can change this to any spacing symbols as preferred
        else:
            visible_result += ch

    print("\n Output (Spaces Shown Visibly):")
    print("Result:", visible_result)

# Output is:
# Enter the original string (can include spaces): Piyush Gopani
# Enter the string to insert: 05

#  Output (Natural Spacing):
# Result: Piyush  05 Gopani

#  Output (Spaces Shown Visibly):
# Result: Piyush␣␣05␣Gopani

# Now this code works as expected: