# 82) Write a Python program to copy the contents of a file to another file.

# Mathod:1:

# Step 1: Ask user for source and destination file names
source_file = input("Enter the source filename (e.g., source.txt): ").strip()
destination_file = input("Enter the destination filename (e.g., copy.txt): ").strip()

try:
    # Step 2: Open the source file in read mode
    with open(source_file, 'r', encoding='utf-8') as src:
        # Read all contents from the source file
        content = src.read()

    # Step 3: Open the destination file in write mode
    with open(destination_file, 'w', encoding='utf-8') as dest:
        # Write the content to the destination file
        dest.write(content)

    # Step 4: Show success message
    print(f"\n✅ Contents of '{source_file}' have been copied to '{destination_file}' successfully.")

except FileNotFoundError:
    # If the source file does not exist
    print(f"❌ File '{source_file}' not found. Please check the filename and try again.")

except Exception as e:
    # Handle any other unexpected errors
    print(f"⚠️ An error occurred: {e}")

# ======================================================================================================================================
# ======================================================================================================================================

# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_82_copy_the_content_of_one_file_to_another.py"
# Enter the source filename (e.g., source.txt): C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp\python_list  
# Enter the destination filename (e.g., copy.txt): C:\Users\Gopani\Desktop\Python Testing.txt  

# ✅ Contents of 'C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp\python_list' have been copied to 'C:\Users\Gopani\Desktop\Python Testing.txt' successfully.
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 

# ======================================================================================================================================
# ======================================================================================================================================

# Mathod :2:

# # 82) Write a Python program to copy the contents of a file to another file

# # Step 1: Ask user for source file and destination file
# source_file = input("Enter the source filename (e.g., source.txt): ").strip()
# destination_file = input("Enter the destination filename (e.g., copy.txt): ").strip()

# try:
#     # Step 2: Open the source file in read mode
#     with open(source_file, 'r', encoding='utf-8') as src:
#         # Step 3: Read the contents of the source file
#         content = src.read()

#     # Step 4: Open the destination file in write mode
#     with open(destination_file, 'w', encoding='utf-8') as dest:
#         # Step 5: Write the contents into the destination file
#         dest.write(content)

#     # Step 6: Print confirmation message
#     print(f"\n✅ Contents of '{source_file}' have been copied to '{destination_file}'")

# except FileNotFoundError:
#     # If the source file doesn't exist
#     print(f"❌ File '{source_file}' not found. Please check the name or path.")
# except Exception as e:
#     # For any other errors
#     print(f"⚠️ An error occurred: {e}")
