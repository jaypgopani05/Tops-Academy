# 77) Read a file line by line and store it into a variable

try:
    filename = input("Enter the filename (e.g., myfile.txt): ").strip()

    # Open the file in read mode with UTF-8 encoding to handle special characters
    with open(filename, 'r', encoding='utf-8') as file:
        content = ""  # Variable to store the file content
        
        # Read each line and append it to 'content'
        for line in file:
            content += line

    # Print the contents stored in the variable 'content'
    print(f"\n📄 Contents of '{filename}' stored in the variable:\n")
    print(content)

except FileNotFoundError:
    print(f"❌ File '{filename}' not found. Please check the file name and path.")
except UnicodeDecodeError:
    print("❌ Unicode decoding error. Please save the file in UTF-8 format.")

# ===================================================================================================================================
# ===================================================================================================================================

# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_77_Read_file_line_by_line_and_store_into_variables.py"
# Enter the filename (e.g., myfile.txt): C:\Users\Gopani\Desktop\Python Testing.txt  

# 📄 Contents of 'C:\Users\Gopani\Desktop\Python Testing.txt' stored in the variable:

#  🔹 1. Introduction
# If you’ve worked with Microsoft Excel, you’ve likely come across the terms Macros and VBA. While many people use them interchangeably, they are not the same.

# In this article, we will explore:

# What macros and VBA actually are

# How they differ

# When it is appropriate to use one over the other

# Real-world scenarios to guide your choice

# 🔹 2. What is a Macro in Excel?
# A macro is a recorded sequence of actions performed in Excel. It allows users to automate repetitive tasks without writing any code.

# 📌 Example:
# Suppose you regularly format a report by bolding headers, applying filters, and aligning text. Instead of doing this manually each time, you can record a macro once and reuse it with a single click.

# ✅ Ideal for: Basic automation tasks that do not require custom logic.

# 🔹 3. What is VBA (Visual Basic for Applications)?
# VBA is a programming language built into Microsoft Office applications, including Excel. It enables users to write code that controls Excel’s behavior, providing far more flexibility than macros alone.

# With VBA, you can implement logical conditions, loops, custom functions, and even interact with other Office applications such as Outlook or Word. 

# 📌 Example:
# If you want Excel to scan hundreds of rows, identify empty cells, and send an email alert for each — you would need to use VBA.


# ✅ Ideal for: Advanced automation, custom workflows, and complex data operations.



# 🔹 4. Key Differences: Macro vs VBA

# Feature Macro   VBA
# Ease of Use     Simple – No coding required     Requires programming knowledge
# Flexibility             Limited to recorded actions     Full control with custom logic
# Functionality           Good for basic tasks    Suitable for complex operations
# Editing Hard to modify  Easily editable in the code editor
# Integration     Excel only      Can interact with other Office apps


# 🔹 5. When Should You Use Each?
# ✅ Use Macros When:
# You need to automate simple, repetitive actions.

# You are not comfortable writing code.

# You want a quick solution without much complexity.

# ✅ Use VBA When:
# Your task requires conditional logic or loops.

# You need to build custom forms or tools.

# You want to automate interactions between Excel and other applications.

# You aim to build scalable and reusable solutions.

# 🔹 6. Real-Life Use Cases
# Task: Applying the same formatting to a monthly report.
# Best Choice: Macro
# Reason: Simple and repeatable

# Task: Sending emails with custom content from Excel Data
# Best Choice: VBA
# Reason: Requires conditional logic and Outlook integration

# Task: Hiding empty rows based on specific criteria
# Best Choice: VBA
# Reason: Conditional behavior needed

# Task: Combining multiple Excel files into one
# Best Choice: VBA
# Reason: Involves looping through files

# 🔹 7. Getting Started
# To record a Macro:
#         Go to View → Macros → Record Macro in Excel.
# To write VBA code:
#         Go to Developer → Visual Basic Editor, or press Alt + F11.

# 🏁 8. Conclusion
# Both Macros and VBA are powerful tools that can save time and improve efficiency.
# If you are just starting out, macros are a great entry point. As your tasks become more complex, learning VBA will allow you to create highly customized and scalable solutions.

# 🔔 Call to Action:
# Have you used macros or VBA in your work? Share your experience or ask questions in the comments — I’d be happy to help!
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 

# ====================================================================================================================================
# ====================================================================================================================================