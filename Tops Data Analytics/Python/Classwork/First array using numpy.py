# Import numpy 
import numpy as np

user_input = input("Enter numbers separated by spaces: ")
user_array = [int(x) for x in user_input.split()]

# Create a NumPy array
arr = np.array(user_array)

# print array statement
# print(arr)
print(user_array)