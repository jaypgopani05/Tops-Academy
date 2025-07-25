# 81) Write a Python program to write a list to a file and then read it back.

# Function to write a list to a file
def write_list_to_file(filename, my_list):
    """
    Writes each item of the list to the given file.
    Each list item is written on a new line.
    """
    try:
        # Open the file in write mode
        with open(filename, 'w', encoding='utf-8') as file:
            # Loop through the list and write each item to the file
            for item in my_list:
                file.write(item + '\n')
        # Print confirmation message
        print(f"\n✅ List has been successfully written to '{filename}'")
    except Exception as e:
        # Handle any error that occurs during writing
        print(f"⚠️ Error while writing to file: {e}")

# Function to read the file and print its contents
def read_file(filename):
    """
    Reads the file line by line and prints the content.
    """
    try:
        # Open the file in read mode
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"\n📄 Contents of '{filename}':")
            print("-" * 40)  # Print a line separator
            # Read and print each line from the file
            for line in file:
                print(line.strip())  # Remove newline characters
    except FileNotFoundError:
        # If the file doesn't exist
        print(f"❌ File '{filename}' not found.")
    except Exception as e:
        # Handle any other error
        print(f"⚠️ Error while reading the file: {e}")

# ---------------------------
# Main Program Starts Here
# ---------------------------

# Ask the user for a file name to write to
filename = input("Enter the filename (e.g., mylist.txt): ")

# Define a sample list to write to the file
my_list = ["Python", "is", "fun", "to", "learn"]

# Call the function to write the list to the file
write_list_to_file(filename, my_list)

# Call the function to read and display the file content
read_file(filename)


# ====================================================================================================================================
# ====================================================================================================================================

# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_80_Count_Frequency_of_word_in_textfile.py"
# Enter the filename (e.g., mylist.txt): python_list

# ✅ List has been successfully written to 'python_list'

# 📄 Contents of 'python_list':
# ----------------------------------------
# Python
# is
# fun
# to
# learn
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 
# ====================================================================================================================================
# ====================================================================================================================================