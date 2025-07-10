# Get input from the user
num1 = int(input("Enter any number: "))

# Check if the number is negative
if num1 < 0:
    print("Factorial does not exist for a negative input numbers.")
elif num1 == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, num1 + 1):
        factorial *= i
    print(f"The factorial of {num1} is {factorial}.")