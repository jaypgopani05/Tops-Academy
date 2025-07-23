# Import Counter class from collections module
from collections import Counter

# Ask user how many key-value pairs they want to enter
n = int(input("How many key-value pairs do you want to enter? "))

# Create empty lists to store keys and values
keys = []
values = []

# Get the keys from user
print("\nEnter keys:")
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    keys.append(key)

# Get the values from user (no type conversion here)
print("\nEnter values:")
for i in range(n):
    value = input(f"Enter value {i+1} for key '{keys[i]}': ")
    values.append(value)

# Create empty dictionary
result_dict = {}

# Fill the dictionary from both lists
for i in range(n):
    result_dict[keys[i]] = values[i]

# Convert dictionary to Counter for matching sample output
result_counter = Counter(result_dict)

# Print the result
print("\nMapped dictionary as Counter:")
print(result_counter)
