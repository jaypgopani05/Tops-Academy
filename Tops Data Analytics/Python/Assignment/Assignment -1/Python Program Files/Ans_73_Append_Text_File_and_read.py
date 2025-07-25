# 1️⃣ Ask the user for the file name to append text to
filename = input("Enter the filename to append text (e.g., notes.txt): ")

# 2️⃣ Ask the user what text they want to append
new_text = input("Enter the text you want to append: ")

try:
    # 3️⃣ Open the file in append mode ('a') to add new text
    with open(filename, 'a') as file:
        file.write(new_text + '\n')  # Add a newline after the text

    # 4️⃣ Reopen the file in read mode to display the full content
    with open(filename, 'r') as file:
        content = file.read()

    # 5️⃣ Print the updated file content
    print("\n📄 Updated File Content:\n")
    print(content)

except FileNotFoundError:
    # 6️⃣ Handle error if file is not found
    print(f"❌ File '{filename}' not found.")
except Exception as e:
    # 7️⃣ Catch any unexpected error
    print(f"❌ An error occurred: {e}")
# =====================================================================================================================================
# =====================================================================================================================================
# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_73_Append_Text_File_and_read.py"
# Enter the filename to append text (e.g., notes.txt): C:\Users\Gopani\Downloads\Desktop files And Folders\cover letter.txt
# Enter the text you want to append: C:\Users\Gopani\Desktop\payment so far.txt

# 📄 Updated File Content:

# Jay Gopani
# 491 Salisbury St,   
# London, ON, N5Y 3B4  
# jaypgopani05@gmail.com]  
# +1-226-239-7907  
  

# Hiring Manager  
# [Company Name]
# [Company Address]
# [City, State, ZIP Code]

# Dear Hiring Manager,

# I am writing to express my interest in the Work from Home Service and Sales position at [Company Name]. With a robust background in customer service, software engineering, and a diverse academic portfolio, I believe my skills and qualifications make me a strong fit for this role.

# Over the last two years, I have developed a solid foundation in customer service, where I honed my communication, problem-solving, and multitasking abilities while delivering exceptional support to clients. This experience has refined my understanding of customer needs and improved my ability to build rapport, resolve issues, and maintain a positive customer experience. Additionally, with three years of experience as a software engineer, I have gained advanced technical skills and a strong ability to troubleshoot and provide solutions to complex problems efficiently.

# My academic background further supports my qualifications for this position. I hold a Bachelor's degree in Computer Engineering, with a strong focus on developing a technical mindset and problem-solving abilities. Furthermore, I have completed three post-graduate qualifications: a Masterâ€™s in Applied Science, a Masterâ€™s in Marketing Management, and a Masterâ€™s in Information and Network Security. This diverse educational experience allows me to approach challenges from multiple perspectives, whether technical, business-related, or security-focused.

# Additionally, I possess a World Education Services (WES) degree equivalency certificate and an IELTS score of 7, which demonstrates my strong English language skills and adaptability in an international work environment.

# I am confident that my combination of customer service expertise, technical proficiency, and broad academic knowledge would be an asset to your team. I am excited about the opportunity to contribute to your organization and bring my problem-solving skills, professionalism, and enthusiasm to the role.

# Thank you for considering my application. I look forward to the possibility of discussing how my experience and qualifications align with the needs of your team.

# Sincerely,
# Jay GopaniC:\Users\Gopani\Desktop\payment so far.txt
# =====================================================================================================================================
# =====================================================================================================================================
