# # Define the list (you can change the values to test)
# my_list = []

# # Check if the list is empty
# if not my_list:
#     print("📭 The list is empty.")
# else:
#     print("📦 The list is NOT empty.") 


# =====================================================================================================================================
# =====================================================================================================================================

# Checking by Taking user Input
# If only space given in user input, it still should show the empty input.

# For empty input show output as below:

# Enter list items (separated by comma or space): 
# 📭 The list is empty.

# If list is not empty then Show the list and show output as below:

# Enter list items (separated by comma or space): 1
# 📦 The list is NOT empty.
# 📝 Items in the list: ['1']

# =====================================================================================================================================

# 🟡 Ask the user to enter items separated by comma or space
user_input = input("Enter list items (separated by comma or space): ").strip()

# ✅ Replace commas with spaces and split the input into items
items = user_input.replace(',', ' ').split()

# ✅ Remove any extra spaces or empty items
cleaned_list = [item.strip() for item in items if item.strip()]

# ✅ Check if the cleaned list is empty
if not cleaned_list:
    print("📭 The list is empty.")
else:
    print("📦 The list is NOT empty.")
    print("📝 Items in the list:", cleaned_list)

