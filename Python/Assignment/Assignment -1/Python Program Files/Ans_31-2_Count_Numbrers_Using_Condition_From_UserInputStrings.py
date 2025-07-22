# From code 31-1 now we are just changing pre defined input with user input.
# And show the output as defined earlier.

# Ask user for input
user_input = input("Enter strings or numbers (separated by space or comma): ").strip()

# Validate empty input
if not user_input:
    print("❌ Error: No input provided.")
    exit()

# Replace commas with spaces, then split by space
items = user_input.replace(',', ' ').split()

# Remove extra spaces or empty entries
items = [item.strip() for item in items if item.strip()]

# Sets to store unique matches
matching_strings = set()
numeric_seen = set()
numeric_duplicates = set()

# Temporary set for checking string matches by lowercase
matched_string_check = set()

# Process each item
for val in items:
    val_stripped = val.strip()

    # Check for strings that start and end with same character (case-insensitive)
    if val_stripped.isalnum() and len(val_stripped) >= 2:
        val_lower = val_stripped.lower()
        if val_lower[0] == val_lower[-1] and val_lower not in matched_string_check:
            matching_strings.add(val_stripped)  # Store original string
            matched_string_check.add(val_lower)  # Avoid case-insensitive duplicates

    # Check for numeric duplicates
    try:
        num = float(val_stripped) if '.' in val_stripped else int(val_stripped)
        if num in numeric_seen:
            numeric_duplicates.add(num)
        else:
            numeric_seen.add(num)
    except ValueError:
        continue  # Skip if not a valid number

# --- Output Section ---
print("\n📊 --- Result Summary ---")

# Matching Strings Output
print("\n🔤 Matching Strings (Alphabetic/Alphanumeric):")
if matching_strings:
    for s in sorted(matching_strings):
        print(" -", s)
else:
    print(" None")

# Duplicate Numbers Output
print("\n🔢 Duplicate Numeric Values:")
if numeric_duplicates:
    for n in sorted(numeric_duplicates):
        print(" -", n)
else:
    print(" None")

# Total Count
total_matches = len(matching_strings) + len(numeric_duplicates)
print(f"\n✅ Total Matching Count (Strings + Duplicates in Numbers): {total_matches}")
# --- End of code ---
# This program has the output accurately user friendly.
# Notes:
# Empty input validated.
# Lower case user input conversion validated.
# Matching string input with all conditions satisfied.
# added numeric and alphanumeric value matching and finds duplicate entries as well.
# Output is well organized and user friendly.