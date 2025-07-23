my_dict = {}
i = 1

while i <= 15:
    my_dict[i] = i
    i = i + 1

print("Dictionary with keys from 1 to 15:")
print(my_dict)
# =======================================================================================================
# If we want user user input it could be written as follows:
# =======================================================================================================
print("---------------------------------------------------------------------------------------------")
print("Re-writing using User-Input")
print("---------------------------------------------------------------------------------------------")

my_dict = {}

limit = int(input("Enter the number of keys (up to 15): "))

i = 1
while i <= limit and i <= 15:
    my_dict[i] = i
    i = i + 1

print("Dictionary with keys from 1 to", limit, ":")
print(my_dict)
