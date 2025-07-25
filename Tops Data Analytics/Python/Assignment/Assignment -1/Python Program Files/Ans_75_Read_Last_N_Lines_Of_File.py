# 75) Read last n lines of a file

try:
    filename = input("Enter the filename (e.g., myfile.txt): ").strip()

    try:
        n = int(input("Enter how many last lines you want to read: ").strip())
    except ValueError:
        print("❌ Please enter a valid integer for number of lines.")
        exit()

    with open(filename, 'r', encoding='utf-8') as file:
        # Read all lines in the file
        lines = file.readlines()

    # If n is greater than the total lines, we read all lines
    last_n_lines = lines[-n:]

    print(f"\n📄 Last {n} lines of '{filename}':\n")
    for index, line in enumerate(last_n_lines, start=1):
        print(f"Line {index}: {line.strip()}")

except FileNotFoundError:
    print(f"❌ File '{filename}' not found. Please check the file name and path.")
except UnicodeDecodeError:
    print("❌ Unicode decoding error. Please save the file in UTF-8 format.")

# ====================================================================================================================================
# ====================================================================================================================================
# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_75_Read_First_N_Lines_Of_File.py"
# Enter the filename (e.g., myfile.txt): C:\Users\Gopani\Desktop\Python Testing.txt  
# Enter how many lines you want to read: 10

# 📄 First 10 lines of 'C:\Users\Gopani\Desktop\Python Testing.txt':

# 🔹 1. Introduction
# If you’ve worked with Microsoft Excel, you’ve likely come across the terms Macros and VBA. While many people use them interchangeably, they are not the same.

# In this article, we will explore:

# What macros and VBA actually are

# How they differ

# When it is appropriate to use one over the other
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 

# ====================================================================================================================================
# ====================================================================================================================================