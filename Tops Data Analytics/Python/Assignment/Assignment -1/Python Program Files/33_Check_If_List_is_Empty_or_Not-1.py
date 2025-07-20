# This script checks if a list is empty and prints a message accordingly.
# Function to check if a list is empty

def is_list_empty(lst):
    return len(lst) == 0

# Example usage
# my_list = []
my_list = input("Enter list elements separated by spaces: ").split()
# Check if the list is empty
# This will print "The list is empty." if the list is empty, otherwise it will print "The list is not empty."
if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
    # You can add more logic here if needed, for example, processing the list or printing its contents.