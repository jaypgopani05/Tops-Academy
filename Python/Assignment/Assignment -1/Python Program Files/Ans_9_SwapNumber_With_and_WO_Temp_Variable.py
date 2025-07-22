# ------------------------------------------------------------------------------------------------
# Program to swap two numbers with using a temporary variable
# ------------------------------------------------------------------------------------------------

# Input two numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swapping with temp variable
temp = a
a = b
b = temp

print("After swapping (with temp):")
print("a =", a)
print("b =", b)

# ------------------------------------------------------------------------------------------------
# Swapping without temp variable
# ------------------------------------------------------------------------------------------------

# Input two numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swapping without temp variable
a, b = b, a

print("After swapping (without temp):")
print("a =", a)
print("b =", b)
# ------------------------------------------------------------------------------------------------