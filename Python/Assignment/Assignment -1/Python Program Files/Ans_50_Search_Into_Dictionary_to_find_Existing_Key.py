# # Predefined Dictionary
# sample_dict = {
#     "name": "Jay",
#     "age": 30,
#     "city": "Ahmedabad",
#     "email": "jay@example.com"
# }

# # 🖨️ Show the dictionary to the user
# print("📘 Current Dictionary:")
# print(sample_dict)

# # 🔍 Ask the user to enter the key they want to check
# key_to_check = input("\n🔎 Enter the key you want to search for: ").strip()

# # ✅ Check if the key exists
# if key_to_check in sample_dict:
#     print(f"✅ The key '{key_to_check}' exists in the dictionary.")
#     print(f"🔹 Value: {sample_dict[key_to_check]}")
# else:
#     print(f"❌ The key '{key_to_check}' does NOT exist in the dictionary.")
# ===================================================================================================================================
# Let's take user input and rewrite the code by giving menu to user to perform multiple tasks using single program.
# Also amking case-insensitive to search,update,delete etc operations.
# Also allowing user to know that count of changes or operations they have made.
# ===================================================================================================================================

def insert_items(original_dict, key_map):
    global update_count
    while True:
        try:
            count = int(input("How many items do you want to insert? "))
            for i in range(count):
                key = input(f"Enter key for item {i + 1}: ").strip()
                value = input(f"Enter value for item {i + 1}: ").strip()

                lower_key = key.lower()
                original_dict[lower_key] = value
                key_map[lower_key] = key  # Store original casing
                update_count += 1
            break
        except ValueError:
            print("❗ Please enter a valid number.")


def sort_items(original_dict, key_map):
    if not original_dict:
        print("⚠️ Dictionary is empty. Please add items first.")
        return
    choice = input("Sort by value:\n1. Ascending\n2. Descending\nChoose 1 or 2: ").strip()
    if choice == '1':
        sorted_items = sorted(original_dict.items(), key=lambda item: item[1])
        print("🔼 Ascending Order:", {key_map[k]: v for k, v in sorted_items})
    elif choice == '2':
        sorted_items = sorted(original_dict.items(), key=lambda item: item[1], reverse=True)
        print("🔽 Descending Order:", {key_map[k]: v for k, v in sorted_items})
    else:
        print("❗ Invalid choice.")


def search_keys(original_dict, key_map):
    if not original_dict:
        print("⚠️ Dictionary is empty.")
        return
    keys = input("Enter key(s) to search (separated by comma or space): ").replace(',', ' ').split()
    for k in keys:
        lk = k.lower()
        if lk in original_dict:
            print(f"✅ Key '{key_map[lk]}' found with value: {original_dict[lk]}")
        else:
            print(f"❌ Key '{k}' not found.")


def update_items(original_dict, key_map):
    global update_count
    key = input("Enter the key to update: ").strip()
    lk = key.lower()
    if lk in original_dict:
        new_value = input("Enter the new value: ")
        original_dict[lk] = new_value
        update_count += 1
        print(f"✅ Key '{key_map[lk]}' updated to '{new_value}'")
    else:
        print(f"❌ Key '{key}' not found.")


def delete_items(original_dict, key_map):
    global update_count
    key = input("Enter the key to delete: ").strip()
    lk = key.lower()
    if lk in original_dict:
        del original_dict[lk]
        del key_map[lk]
        update_count += 1
        print(f"🗑️ Key '{key}' deleted.")
    else:
        print(f"❌ Key '{key}' not found.")


def concatenate_by_key(original_dict, key_map):
    keys = input("Enter keys to concatenate values (comma or space separated): ").replace(',', ' ').split()
    concat = ''
    for k in keys:
        lk = k.lower()
        if lk in original_dict:
            concat += str(original_dict[lk])
        else:
            print(f"❌ Key '{k}' not found. Skipping.")
    print(f"🔗 Concatenated value: {concat}")


def display_dictionary(original_dict, key_map):
    if not original_dict:
        print("⚠️ Dictionary is empty.")
    else:
        print("📘 Current Dictionary Contents:")
        for k in original_dict:
            print(f"🔹 {key_map[k]} : {original_dict[k]}")


# Main program
dictionary = {}
key_casing_map = {}
task_count = 0
update_count = 0

print("\n📌 Dictionary Management Program")
print("🧠 Manage your dictionary interactively!\n")

while True:
    if not dictionary:
        print("-------------------------------------------------------------------------")
        print("⚠️ You have to insert some values first to perform any operations from Menu:")
        print("-------------------------------------------------------------------------")

    print("\n📋 MENU:")
    print("1. Insert items")
    print("2. Sort items (ascending or descending)")
    print("3. Search key(s)")
    print("4. Update items")
    print("5. Delete items")
    print("6. Concatenate items by key")
    print("7. Display current dictionary")
    print("8. Exit")

    choice = input("Choose an option (1-8): ").strip()

    if choice == '1':
        task_count += 1
        insert_items(dictionary, key_casing_map)
    elif choice == '2':
        task_count += 1
        sort_items(dictionary, key_casing_map)
    elif choice == '3':
        task_count += 1
        search_keys(dictionary, key_casing_map)
    elif choice == '4':
        task_count += 1
        update_items(dictionary, key_casing_map)
    elif choice == '5':
        task_count += 1
        delete_items(dictionary, key_casing_map)
    elif choice == '6':
        task_count += 1
        concatenate_by_key(dictionary, key_casing_map)
    elif choice == '7':
        task_count += 1
        display_dictionary(dictionary, key_casing_map)
    elif choice == '8':
        print("\n👋 Exiting the program...")
        print(f"📊 You performed *{task_count}* task(s) from the menu.")
        print(f"📦 You updated the dictionary *{update_count}* time(s).")
        print("✅ Program ended successfully.")
        break
    else:
        print("❗ Invalid option. Please choose between 1-8.")
