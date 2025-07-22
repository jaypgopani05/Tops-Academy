import re

try:
    # Take input from the user
    user_input = input("Enter list elements (comma or space separated): ").strip()

    # Validate input
    if not user_input:
        raise ValueError("List cannot be empty. Please enter at least 2 elements.")

    # Split input using regex to handle comma or space
    input_list = [item.strip() for item in re.split(r'[,\s]+', user_input) if item.strip()]

    # Ensure there are at least 2 elements
    if len(input_list) < 2:
        raise ValueError("Please enter at least two items to split into variables.")

    # Create a dictionary to store variables like var1, var2, var3, ...
    variable_dict = {}

    for idx, value in enumerate(input_list):
        var_name = f"var{idx+1}"
        variable_dict[var_name] = value

    # Print all variable names and their values
    print("\n✅ Variables assigned dynamically:")
    for key, value in variable_dict.items():
        print(f"{key} = {value}")

except Exception as e:
    print("⚠️ Error:", e)
