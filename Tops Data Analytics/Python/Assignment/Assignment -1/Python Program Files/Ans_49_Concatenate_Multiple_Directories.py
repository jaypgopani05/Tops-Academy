# # concatenate multiple dictionaries

# # Sample dictionaries to merge (you can also take from user input if needed)
# dict1 = {'a': 100, 'b': 200}
# dict2 = {'c': 300, 'd': 400}
# dict3 = {'e': 500, 'f': 600}

# # 🧠 Use update() to merge all into a new dictionary
# combined_dict = {}

# # ✅ Merging one by one
# combined_dict.update(dict1)
# combined_dict.update(dict2)
# combined_dict.update(dict3)

# # 🎯 Final merged dictionary
# print("📌 Dictionary 1:", dict1)
# print("📌 Dictionary 2:", dict2)
# print("📌 Dictionary 3:", dict3)
# print("\n✅ Combined Dictionary:")
# print(combined_dict)

# ---End of Code---
# Let's take user input for directories and concatenate all togather

# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

# Script to combine multiple user-defined dictionaries

def get_user_dictionary(index):
    """
    Function to get a dictionary from the user
    """
    # if index<2:
    #     print("-------------------------------------------------------------------------------------------")
    #     print("Empty Directory is found. Please insert some values to merge with different Directories:")
    #     print("-------------------------------------------------------------------------------------------")
    # else:
    #     print("Enter more data to create directories:")

    user_dict = {}

    while True:
        try:
                       
            count = input(f"\nHow many items in Dictionary from Directory Number::{index}? (or type 'exit' to quit): ").strip()
            if count.lower() == 'exit':
                print(f"Exiting the program you have added {index} Directories:")
                return None
            count = int(count)
            if count <= 0:
                print("⚠️ Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("❗ Please enter a valid number.")

    for i in range(1, count + 1):
        print(f"\n➡️ Enter details for item {i}:")
        key = input("Enter key (text only, Ex: names, Subjects etc.): ").strip()
        value = input("Enter value(Number only, Ex: Enrollment Number, Roll Number, Phone Number etc.): ").strip()
        user_dict[key] = value  # everything stored as string for simplicity

    return user_dict


# 🧠 Main logic
final_dict = {}
dict_count = 1

print("\n📌 This program concatenates multiple dictionaries provided by you.")

if dict_count<2:
        print("-------------------------------------------------------------------------------------------")
        print("Empty Directory is found. Please insert some values to merge with different Directories:")
        print("-------------------------------------------------------------------------------------------")
else:
        print("Enter more data to create directories:")

while True:
    result = get_user_dictionary(dict_count)
    if result is None:
        break  # user typed 'exit'
    final_dict.update(result)
    dict_count += 1

    # Ask if user wants to continue
    next_action = input("\n Do you want to add another dictionary? (yes/no): ").strip().lower()
    if next_action != 'yes':
        break

# ✅ Final Output
print("\n✅ Final Combined Dictionary:")
print(final_dict)

# -------------------------------------------------------------------------------------------------------------------------------------
# Sample Output:
# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

#📌 This program concatenates multiple dictionaries provided by you.
# -------------------------------------------------------------------------------------------
# Empty Directory is found. Please insert some values to merge with different Directories:
# -------------------------------------------------------------------------------------------

# How many items in Dictionary from Directory Number::1? (or type 'exit' to quit): 2  

# ➡️ Enter details for item 1:
# Enter key (text only, Ex: names, Subjects etc.): Jay
# Enter value(Number only, Ex: Enrollment Number, Roll Number, Phone Number etc.): 101

# ➡️ Enter details for item 2:
# Enter key (text only, Ex: names, Subjects etc.): Bhavesh
# Enter value(Number only, Ex: Enrollment Number, Roll Number, Phone Number etc.): 102

#  Do you want to add another dictionary? (yes/no): yes

# How many items in Dictionary from Directory Number::2? (or type 'exit' to quit): exit
# Exiting the program you have added 2 Directories:

# ✅ Final Combined Dictionary:
# {'Jay': '101', 'Bhavesh': '102'} 
