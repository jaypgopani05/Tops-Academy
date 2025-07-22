# Function to check if sublist exists in main list (case-insensitive)
def is_sublist_case_insensitive(main_list, sub_list):
    # Convert both lists to lowercase versions for comparison
    lower_main = [item.lower() for item in main_list]
    lower_sub = [item.lower() for item in sub_list]

    m, n = len(lower_main), len(lower_sub)

    # Slide over main list to check for a matching sequence
    for i in range(m - n + 1):
        if lower_main[i:i+n] == lower_sub:
            return True, i  # Return match found and position
    return False, -1  # Not found

# Main program
try:
    import re

    # Get main list from user
    main_input = input("Enter main list items (comma or space-separated): ").strip()
    if not main_input:
        raise ValueError("Main list cannot be empty.")
    main_list = [item.strip() for item in re.split(r'[,\s]+', main_input) if item.strip()]

    # Get sublist from user
    sub_input = input("Enter sublist to search (comma or space-separated): ").strip()
    if not sub_input:
        raise ValueError("Sublist cannot be empty.")
    sub_list = [item.strip() for item in re.split(r'[,\s]+', sub_input) if item.strip()]

    if len(sub_list) > len(main_list):
        raise ValueError("Sublist cannot be longer than main list.")

    # Perform case-insensitive check
    found, index = is_sublist_case_insensitive(main_list, sub_list)

    # Output results
    print("\n✅ Main List:", main_list)
    print("🔍 Sublist to Search:", sub_list)

    if found:
        # Show matched segment from original main list
        matched_segment = main_list[index:index+len(sub_list)]
        print(f"✅ Match Found: {sub_list} matches with {matched_segment} (case-insensitive)")
    else:
        print("❌ No match found.")

except Exception as e:
    print("⚠️ Error:", e)

