# 34) Write a Python function that takes two lists and returns true if they have at least one common member. 

# 🔁 Function to check and return common members (case-insensitive)
def find_common_members(list1, list2):
    common = []  # Store original case of common elements
    seen = set()  # Track lowercase matches
    list2_lower = [item.lower() for item in list2]

    for item in list1:
        if item.lower() in list2_lower and item.lower() not in seen:
            common.append(item)
            seen.add(item.lower())  # Avoid duplicates (like "tops" and "Tops")

    return common

# 📥 Take user input for both lists
input1 = input("Enter items for first list (comma or space separated): ")
input2 = input("Enter items for second list (comma or space separated): ")

# 🧹 Clean and split inputs into lists
list1 = [item.strip() for item in input1.replace(',', ' ').split() if item.strip()]
list2 = [item.strip() for item in input2.replace(',', ' ').split() if item.strip()]

# 🔍 Find common members (case-insensitive)
common_items = find_common_members(list1, list2)

# ✅ Output the result
if common_items:
    print("\n✅ The lists have at least", len(common_items),  "common member.")
    print("🔁 Common members (case-insensitive):")
    for item in common_items:
        print("-", item)
else:
    print("\n❌ The lists do not have any common members.")