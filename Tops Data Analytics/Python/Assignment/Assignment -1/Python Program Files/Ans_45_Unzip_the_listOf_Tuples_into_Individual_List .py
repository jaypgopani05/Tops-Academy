def get_tuple_input():
    # Ask how many tuples the user wants to enter
    while True:
        try:
            print("Note: Please use only numbers and separated by coma.")
            n = int(input("How many tuples? "))
            if n < 1:
                print("⚠️ Enter at least 1 tuple.")
                continue
            break
        except ValueError:
            print("❌ Invalid number. Please enter a valid integer.")
    
    tuple_list = []

    for i in range(n):
        while True:
            raw = input(f"Enter tuple #{i+1} (comma-separated values): ")
            parts = [p.strip() for p in raw.split(',') if p.strip()]
            if len(parts) < 2:
                print("⚠️ Please enter at least 2 values per tuple.")
                continue
            tuple_list.append(tuple(parts))
            break

    return tuple_list

# Main Program
print("🔄 Unzip a List of Tuples into Separate Lists")

tuples = get_tuple_input()

# Show original
print("\nOriginal list of tuples:", tuples)

# Unzipping using zip(*...)
unzipped = list(zip(*tuples))

# Show each list
print("\nUnzipped lists:")
for i, lst in enumerate(unzipped, start=1):
    print(f"List {i}: {list(lst)}")
