    # 79) Write a Python program to count the number of lines in a text file.

# Step 1: Ask user to enter the file path or name
filename = input("Enter the filename with full path (e.g., C:/Users/YourName/Desktop/myfile.txt): ")

try:
    # Step 2: Open the file in read mode
    with open(filename, 'r', encoding='utf-8') as file:
        # Step 3: Read all lines and count them
        lines = file.readlines()
        line_count = len(lines)
        
        # Step 4: Print the total number of lines
        print(f"📄 Total number of lines in '{filename}': {line_count}")

except FileNotFoundError:
    # If the file is not found, print an error message
    print("❌ File not found. Please check the file name and path.")

except Exception as e:
    # For any other unexpected errors
    print(f"⚠️ An error occurred: {e}")

# =====================================================================================================================================
# =====================================================================================================================================

# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_79_Count_nos_of_lines_in_textfile.py"
# Enter the filename with full path (e.g., C:/Users/YourName/Desktop/myfile.txt): C:\Users\Gopani\Desktop\Python Testing.txt  
# 📄 Total number of lines in 'C:\Users\Gopani\Desktop\Python Testing.txt': 90
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 

# ======================================================================================================================================
# ======================================================================================================================================
