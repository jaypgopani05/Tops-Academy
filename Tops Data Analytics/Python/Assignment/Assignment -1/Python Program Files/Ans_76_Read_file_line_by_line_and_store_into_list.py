# 76) Read a file line by line and store into a list

try:
    filename = input("Enter the filename (e.g., myfile.txt): ").strip()

    with open(filename, 'r', encoding='utf-8') as file:
        lines_list = file.readlines()

    print(f"\n📄 Contents of '{filename}' stored in a list:\n")
    for index, line in enumerate(lines_list, start=1):
        print(f"Line {index}: {line.strip()}")

except FileNotFoundError:
    print(f"❌ File '{filename}' not found. Please check the path.")
except UnicodeDecodeError:
    print("❌ Unicode decoding error. Please save the file in UTF-8 format.")
# =====================================================================================================================================
# =====================================================================================================================================
# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_76_Read_file_line_by_line_and_store_into_list.py"
# Enter the filename (e.g., myfile.txt): C:\Users\Gopani\Desktop\Python Testing.txt  

# 📄 Contents of 'C:\Users\Gopani\Desktop\Python Testing.txt' stored in a list:

# Line 1: 🔹 1. Introduction
# Line 2: If you’ve worked with Microsoft Excel, you’ve likely come across the terms Macros and VBA. While many people use them interchangeably, they are not the same.
# Line 3: 
# Line 4: In this article, we will explore:
# Line 5: 
# Line 6: What macros and VBA actually are
# Line 7: 
# Line 8: How they differ
# Line 9:
# Line 10: When it is appropriate to use one over the other
# Line 11:
# Line 12: Real-world scenarios to guide your choice
# Line 13:
# Line 14: 🔹 2. What is a Macro in Excel?
# Line 15: A macro is a recorded sequence of actions performed in Excel. It allows users to automate repetitive tasks without writing any code.      
# Line 16:
# Line 17: 📌 Example:
# Line 18: Suppose you regularly format a report by bolding headers, applying filters, and aligning text. Instead of doing this manually each time, you can record a macro once and reuse it with a single click.
# Line 19:
# Line 20: ✅ Ideal for: Basic automation tasks that do not require custom logic.
# Line 21:
# Line 22: 🔹 3. What is VBA (Visual Basic for Applications)?
# Line 23: VBA is a programming language built into Microsoft Office applications, including Excel. It enables users to write code that controls Excel’s behavior, providing far more flexibility than macros alone.
# Line 24:
# Line 25: With VBA, you can implement logical conditions, loops, custom functions, and even interact with other Office applications such as Outlook or Word.
# Line 26:
# Line 27: 📌 Example:
# Line 28: If you want Excel to scan hundreds of rows, identify empty cells, and send an email alert for each — you would need to use VBA.
# Line 29:
# Line 30:
# Line 31: ✅ Ideal for: Advanced automation, custom workflows, and complex data operations.
# Line 32:
# Line 33:
# Line 34:
# Line 35: 🔹 4. Key Differences: Macro vs VBA
# Line 36:
# Line 37: Feature        Macro   VBA
# Line 38: Ease of Use    Simple – No coding required     Requires programming knowledge
# Line 39: Flexibility            Limited to recorded actions     Full control with custom logic
# Line 40: Functionality          Good for basic tasks    Suitable for complex operations
# Line 41: Editing        Hard to modify  Easily editable in the code editor
# Line 42: Integration    Excel only      Can interact with other Office apps
# Line 43:
# Line 44:
# Line 45: 🔹 5. When Should You Use Each?
# Line 46: ✅ Use Macros When:
# Line 47: You need to automate simple, repetitive actions.
# Line 48:
# Line 49: You are not comfortable writing code.
# Line 50:
# Line 51: You want a quick solution without much complexity.
# Line 52:
# Line 53: ✅ Use VBA When:
# Line 54: Your task requires conditional logic or loops.
# Line 55:
# Line 56: You need to build custom forms or tools.
# Line 57:
# Line 58: You want to automate interactions between Excel and other applications.
# Line 59:
# Line 60: You aim to build scalable and reusable solutions.
# Line 61:
# Line 62: 🔹 6. Real-Life Use Cases
# Line 63: Task: Applying the same formatting to a monthly report.
# Line 64: Best Choice: Macro
# Line 65: Reason: Simple and repeatable
# Line 66:
# Line 67: Task: Sending emails with custom content from Excel Data
# Line 68: Best Choice: VBA
# Line 69: Reason: Requires conditional logic and Outlook integration
# Line 70:
# Line 71: Task: Hiding empty rows based on specific criteria
# Line 72: Best Choice: VBA
# Line 73: Reason: Conditional behavior needed
# Line 74:
# Line 75: Task: Combining multiple Excel files into one
# Line 76: Best Choice: VBA
# Line 77: Reason: Involves looping through files
# Line 78:
# Line 79: 🔹 7. Getting Started
# Line 80: To record a Macro:
# Line 81: Go to View → Macros → Record Macro in Excel.
# Line 82: To write VBA code:
# Line 83: Go to Developer → Visual Basic Editor, or press Alt + F11.
# Line 84:
# Line 85: 🏁 8. Conclusion
# Line 86: Both Macros and VBA are powerful tools that can save time and improve efficiency.
# Line 87: If you are just starting out, macros are a great entry point. As your tasks become more complex, learning VBA will allow you to create highly customized and scalable solutions.
# Line 88:
# Line 89: 🔔 Call to Action:
# Line 90: Have you used macros or VBA in your work? Share your experience or ask questions in the comments — I’d be happy to help!
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 

# =====================================================================================================================================
# =====================================================================================================================================