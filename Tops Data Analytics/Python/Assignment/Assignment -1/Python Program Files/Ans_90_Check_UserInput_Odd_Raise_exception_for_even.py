# Function to get only an odd number from the user
def get_odd_number():
    while True:
        try:
            # Ask for input
            num = int(input("Enter an odd number: "))
            
            # Check for even number
            if num % 2 == 0:
                raise ValueError("❌ Even number entered! Please try again.")
            
            # If it's odd, break the loop
            print(f"✅ You entered a valid odd number: {num}")
            break

        except ValueError as ve:
            print(ve)  # Display error message and continue loop

# Call the function
get_odd_number()

# ======================================================================================================================================
# ======================================================================================================================================

# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_90_Check_UserInput_Odd_Raise_exception_for_even.py"
# Enter an odd number: 22
# ❌ Even number entered! Please try again.
# Enter an odd number: 21
# ✅ You entered a valid odd number: 21
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp>
# 
# =======================================================================================================================================
# ======================================================================================================================================= 