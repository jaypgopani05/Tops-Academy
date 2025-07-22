def detect_data_type(value):
    """Try to detect and convert the input to int, float, bool, or leave as string."""
    val = value.strip()

    # Check for boolean (case-insensitive)
    if val.lower() == 'true':
        return True
    elif val.lower() == 'false':
        return False

    # Check for integer
    try:
        return int(val)
    except ValueError:
        pass

    # Check for float
    try:
        return float(val)
    except ValueError:
        pass

    # Fallback to string
    return val

# Main program
print("🔄 Create a Tuple with Auto-detected Data Types")

try:
    num_items = int(input("How many values do you want to enter? "))
    if num_items < 1:
        raise ValueError("You must enter at least 1 value.")

    elements = []
    for i in range(num_items):
        raw_value = input(f"Enter value #{i + 1}: ")
        typed_value = detect_data_type(raw_value)
        elements.append(typed_value)

    result_tuple = tuple(elements)

    print("\n✅ Final Tuple with Auto-detected Data Types:")
    print(result_tuple)
    print("📌 Data Types in Tuple:")
    for item in result_tuple:
        print(f"{item} ({type(item).__name__})")

except Exception as e:
    print("⚠️ Error:", e)
