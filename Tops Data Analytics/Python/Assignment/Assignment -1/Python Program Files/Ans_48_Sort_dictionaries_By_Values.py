# program to sort a dictionary with smart menu

print("📌 Welcome to Dictionary Sorter!")

my_dict = {}

def get_dict_entries():
    while True:
        num = input("\nHow many items do you want to add to the dictionary? (or type 'exit' to quit): ").strip()
        if num.lower() == 'exit':
            print("👋 Exiting the program. Goodbye!")
            exit()
        if num.isdigit() and int(num) > 0:
            num = int(num)
            break
        else:
            print("❌ Please enter a valid positive number.")

    for i in range(num):
        print(f"\nEnter details for item {i + 1} (or type 'exit' to quit):")
        
        key = input("Enter key (name): ").strip()
        if key.lower() == 'exit':
            print("👋 Exiting the program. Goodbye!")
            exit()

        while True:
            value = input("Enter value (number only): ").strip()
            if value.lower() == 'exit':
                print("👋 Exiting the program. Goodbye!")
                exit()
            if value.isdigit():
                value = int(value)
                break
            else:
                print("❌ Value must be a number.")

        my_dict[key] = value

def sort_and_show():
    while True:
        print("\n📌 Current Dictionary:")
        print(my_dict)

        print("\nHow would you like to sort the dictionary?")
        print("1. Ascending (Lowest to Highest)")
        print("2. Descending (Highest to Lowest)")
        sort_choice = input("Enter 1 or 2 (or type 'exit' to quit): ").strip().lower()

        if sort_choice == 'exit':
            print("👋 Exiting the program. Goodbye!")
            exit()
        elif sort_choice == '1':
            sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
            print("\n🔼 Dictionary Sorted by Value (Ascending):")
            print(sorted_dict)
            break
        elif sort_choice == '2':
            sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
            print("\n🔽 Dictionary Sorted by Value (Descending):")
            print(sorted_dict)
            break
        else:
            print("❌ Invalid input. Please enter 1, 2, or 'exit'.")

# 🚀 Main Loop
while True:
    if not my_dict:
        get_dict_entries()

    sort_and_show()

    while True:
        print("\nWhat would you like to do next?")
        print("1. Sort again")
        print("2. Add more data")
        print("3. Exit")
        next_step = input("Enter choice (1/2/3): ").strip()

        if next_step == '1':
            sort_and_show()  # Immediately go to sorting
        elif next_step == '2':
            get_dict_entries()
            break  # back to sort after new data
        elif next_step == '3':
            print("👋 Exiting the program. Goodbye!")
            exit()
        else:
            print("❌ Please enter 1, 2, or 3.")
