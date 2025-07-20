# # 🎯 Create a list of squares from 1 to 30
# squares = [x**2 for x in range(1, 31)]

# # ✅ Print the complete list (optional)
# print("🔢 All Squares from 1 to 30:")
# print(squares)

# # 🖨️ Print the first 5 elements
# print("\n🔝 First 5 Elements:")
# print(squares[:5])

# # 🖨️ Print the last 5 elements
# print("\n🔚 Last 5 Elements:")
# print(squares[-5:])
# ======================================================================================================
# Now taking user input to generate list
# ======================================================================================================

# 📝 Ask user to enter a number for the upper limit
try:
    upper_limit = int(input("Enter a number to generate squares from 1 to that number: "))
    
    # ✅ Check if number is valid
    if upper_limit < 1:
        print("❌ Please enter a number greater than 0.")
    else:
        # 🎯 Generate list of squares
        squares = [x**2 for x in range(1, upper_limit + 1)]
        
        # 📋 Show all squares (optional)
        print("\n📋 All Squares:")
        print(squares)

        # 🖨️ First 5 squares
        print("\n🔝 First 5 Squares:")
        print(squares[:5])

        # 🖨️ Last 5 squares
        print("\n🔚 Last 5 Squares:")
        print(squares[-5:])

except ValueError:
    print("❌ Invalid input. Please enter a valid integer.")
