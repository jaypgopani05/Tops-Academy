# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# for i in range(num1, num2 + 1):
#     print(i)
# =================================================================================================================

# This code takes two integers as input and prints all the numbers from the first to the second, inclusive.
# It uses a for loop to iterate through the range from num1 to num2 and prints each number.
# =================================================================================================================
# =================================================================================================================

# user_input=int(input("Enter a number: "))
# User_input2 = int(input("Enter another number: "))
# list=[1,22,3,45,60,43,90,112,333,1000,2000,3000,4000,5000]
# for i in list:
#     if i % 3 == 0:
#         print(i)   

# =================================================================================================================
# This code takes two integers as input and prints all the numbers between them that are divisible by 3.
# It uses a for loop to iterate through the range from user_input to User_input2 and checks if each number is divisible by 3.
# If it is, the number is printed.
# =================================================================================================================
# =================================================================================================================

# This code takes an integer input from the user and prints the multiplication table for that number from 1 to 10.
# It uses a for loop to iterate through the numbers 1 to 10 and prints the product of the user input and the current loop index.
# The output is formatted to show the multiplication in a readable way.
# =================================================================================================================
# =================================================================================================================

# Function to classify even and odd numbers in a list
def classify_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

# Example list:
numbers_list = [3,4,5,56,78,99,23,123,456,100,120,145]
classify_even_odd(numbers_list)
even_count = 0
odd_count = 0
for num in numbers_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Total Even numbers: {even_count}")
print(f"Total Odd numbers: {odd_count}")
# =================================================================================================================
# This code defines a function that takes a list of numbers and classifies each number as even or odd.
# It uses a for loop to iterate through the list and checks if each number is divisible by 2.
# The result is printed in a readable format indicating whether each number is even or odd.
# =================================================================================================================