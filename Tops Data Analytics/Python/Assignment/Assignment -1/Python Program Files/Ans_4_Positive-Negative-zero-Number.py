# Program to check if the user input number is positive, negative or zero

num1 = float(input("Enter any Positive, Negative or Zero numbers here: "))
# Convert the STRING Number into floating-point number.

if num1 > 0:
    print("Your given input number is positive.")    
    # Check if the number is greater than zero.

elif num1 < 0:
    print("Your given input number is negative.")
# Check if the number is less than to zero.

else:
    print("Your given input number is zero.")
    # print if the number is equal to zero.