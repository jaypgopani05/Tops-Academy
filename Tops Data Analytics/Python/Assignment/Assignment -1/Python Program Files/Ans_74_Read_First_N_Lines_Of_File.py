# Read First N Lines of a File

try:
    filename = input("Enter the filename (e.g., myfile.txt): ").strip()
    try:
        n = int(input("Enter how many lines you want to read: ").strip())
    except ValueError:
        print("❌ Please enter a valid integer for number of lines.")
        exit()

    print(f"\n📄 First {n} lines of '{filename}':\n")

    with open(filename, 'r', encoding='utf-8') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line.strip())

except FileNotFoundError:
    print(f"❌ File '{filename}' not found. Please check the file name and path.")

except UnicodeDecodeError:
    print(f"❌ Unable to decode file '{filename}'. Try saving it in UTF-8 format.")
# ====================================================================================================================================
# ====================================================================================================================================
# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_74_Read_First_N_Lines_Of_File.py"
# Enter the filename (e.g., myfile.txt): C:\Users\Gopani\Desktop\Python Testing.txt  
# Enter how many lines you want to read: 5

# 📄 First 5 lines of 'C:\Users\Gopani\Desktop\Python Testing.txt':

# 🔹 1. Introduction
# If you’ve worked with Microsoft Excel, you’ve likely come across the terms Macros and VBA. While many people use them interchangeably, they are not the same.

# In this article, we will explore:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 

# ====================================================================================================================================
# ====================================================================================================================================