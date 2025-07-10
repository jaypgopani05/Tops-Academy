# Get input from the user
user_input = input("Enter Your Input Here: ")

try:
    # Try converting to float
    num = float(user_input)

    # Check for zero
    if num == 0:
        print("You entered zero. Please enter a non-zero number.")

    # Check if number is a whole number (integer)
    elif num.is_integer():
        num = int(num)  # Safe to convert to int

        if num > 0:
            if num % 2 == 0:
                print(f"{num} is a Positive Even number.")
            else:
                print(f"{num} is a Positive Odd number.")
        else:
            if num % 2 == 0:
                print(f"{num} is a Negative Even number.")
            else:
                print(f"{num} is a Negative Odd number.")
    else:
        # If it's a float, but not an integer
        if num > 0:
            print(f"{num} is a Positive Float number. Cannot classify as Even or Odd.")
        else:
            print(f"{num} is a Negative Float number. Cannot classify as Even or Odd.")

except ValueError:
    print("Invalid input! Please enter a numeric value.")

# Negative or Positive Float numbers Cannot classify as even or odd, only integer numbers can be classified as even or odd.
# If the input is not a number, it will raise a ValueError and print an error message.
# If the input is zero, it will prompt the user to enter a non-zero number.