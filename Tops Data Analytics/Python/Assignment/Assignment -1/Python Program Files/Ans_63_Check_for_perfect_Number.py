# Function to check if a number is perfect
# A number is perfect if the sum of its proper divisors equals the number itself
def is_perfect_number(n):
    if n <= 0:
        return False  # Negative numbers and 0 are not perfect numbers

    sum_of_divisors = 0  # Initialize sum of divisors to 0

    # Loop to find all divisors from 1 to n-1 (excluding the number itself)
    for i in range(1, n):
        if n % i == 0:  # If i divides n completely, it's a divisor
            sum_of_divisors += i  # Add the divisor to the sum

    # Return True if the sum of divisors is equal to the original number
    return sum_of_divisors == n

# -------- Main Program --------

# Loop until user enters a valid positive integer
while True:
    try:
        # Ask the user to enter a number to check
        num = int(input("Enter a positive number to check if it is perfect: "))

        # Validate if the number is greater than 0
        if num <= 0:
            print("❌ Please enter a positive number greater than 0.")
        else:
            break  # Exit loop if valid input is received
    except ValueError:
        # Handle the case where user enters non-integer value
        print("❌ Invalid input! Please enter a valid integer.")

# Call the function and print whether the number is perfect or not
if is_perfect_number(num):
    print(f"✅ Yes, {num} is a Perfect Number.")
else:
    print(f"❌ No, {num} is NOT a Perfect Number.")

# Note:
# A perfect number is as below:
# user input : 6
# Output: 6 is a perfect number.
# Because n=6 and i(Divisors of number 6 are:): 1,2,3
# Sum of i =1+2+3=6
# Thus n=i and number 6 is a perfect number.