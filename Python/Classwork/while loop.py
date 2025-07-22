# i=1
# while i < 10:
#     if i%2==0:
#         print(i,"is Even")
#     else:
#         print(i,"is odd")
#     i=i+1

# num = int(input("Enter a number to print its multiplication table: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1

# ==================================================================================================================
# ==================================================================================================================

# # Reverse the multiplication table output
# nums = input("Enter numbers separated by space or comma to print their multiplication tables in reverse: ")
# nums = [int(n) for n in nums.replace(',', ' ').split()]
# for num in nums:
#     i = 10
#     while i >= 1:
#         print(f"{num} x {i} = {num * i}")
#         i -= 1
#     print("-" * 20)
# count = int(input("How many numbers do you want to print the reverse multiplication table for? "))
# for _ in range(count):
#     num2 = int(input("Enter a number to print its multiplication table in reverse: "))
#     i = 10
#     while i >= 1:
#         print(f"{num2} x {i} = {num2 * i}")
#         i -= 1
#     print("-" * 20)
#     print("\n🧮 Reverse Multiplication Tables:\n")

# ==============================================================================================================
# ==============================================================================================================

# # Function to generate reverse multiplication table
# def get_reverse_table(num):
#     table = []
#     for i in range(10, 0, -1):
#         line = f"{num} x {i:<2} = {num * i:<3}"
#         table.append(line)
#     return table
#     # Get input from user
# user_input = input("Enter numbers separated by space or comma: ")
# nums = [int(n) for n in user_input.replace(',', ' ').split()]
# # Store tables for all numbers
# tables = [get_reverse_table(n) for n in nums]
#     # Print tables side by side
# for row in range(10):  # Each table has 10 lines
#     line = ""
#     for col in range(len(tables)):
#         line += tables[col][row].ljust(20) + "|   "
#     print(line.rstrip())

# print("\n✅ Done!")
# ===========================================================================================================
# ===========================================================================================================


# Function to generate a reverse multiplication table for a number using a for loop
def get_reverse_table_for(num):
    table = []
    for i in range(10, 0, -1):  # From 10 to 1
        line = f"{num} x {i:<2} = {num * i:<3}"
        table.append(line)
    return table

# Function to generate a reverse multiplication table for a number using a while loop
def get_reverse_table_while(num):
    table = []
    i = 10
    while i >= 1:
        line = f"{num} x {i:<2} = {num * i:<3}"
        table.append(line)
        i -= 1
    return table

user_input = input("Enter numbers separated by space or comma: ")
nums = [int(n) for n in user_input.replace(',', ' ').split()]

if len(nums) > 5:
    print("❗Warning: Please enter 5 numbers maximum.")
    exit()

# Choose which loop to use for demonstration
use_for = True  # Change to False to use while loop

tables = []
for n in nums:
    if use_for:
        tables.append(get_reverse_table_for(n))
    else:
        tables.append(get_reverse_table_while(n))

print("\n🧮 Reverse Multiplication Tables:\n")
for row in range(10):
    line = ""
    for col in range(len(tables)):
        line += tables[col][row].ljust(24) + "|   "
    print(line.rstrip())

print("\n👍 Done!")