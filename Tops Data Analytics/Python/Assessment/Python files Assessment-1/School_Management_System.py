# Global dictionary to store student records, with student ID as the key
students = {}

# Global variable to assign the next unique student ID
next_id = 1

# Function to handle new student admission
def new_admission():
    global next_id  # Use global variable to update student ID

    # Ask for student name
    name = input("Student Name: ").strip()  # Remove extra spaces

    try:
        # Ask for student age and convert to integer
        age = int(input("Age (5–18): "))
        # Validate age range
        if not 5 <= age <= 18:
            print("Age must be between 5 and 18.")
            return  # Stop if invalid

        # Ask for student class and convert to integer
        class_level = int(input("Class (1–12): "))
        # Validate class range
        if not 1 <= class_level <= 12:
            print("Class must be between 1 and 12.")
            return  # Stop if invalid

    except ValueError:
        # Handle invalid number input
        print("Invalid numeric input.")
        return

    # Ask for guardian's mobile number
    mobile = input("Guardian's Mobile (10 digits): ").strip()

    # Validate mobile number
    if not (mobile.isdigit() and len(mobile) == 10):
        print("Invalid mobile number.")
        return  # Stop if invalid

    # Add the new student to the dictionary
    students[next_id] = {
        "Name": name,
        "Age": age,
        "Class": class_level,
        "Mobile": mobile
    }

    # Display confirmation
    print(f"\nAdmission Successful. Student ID: {next_id}")

    # Show full student record
    display_student(next_id)

    # Increment student ID for next admission
    next_id += 1


# Function to display a specific student's details
def display_student(sid):
    # Fetch student details using the ID
    student = students.get(sid)

    # If student exists, display their info
    if student:
        print(f"\n--- Student ID: {sid} ---")
        # Loop through student dictionary and print each key-value pair
        for key, value in student.items():
            print(f"{key}: {value}")
        print("-------------------------\n")
    else:
        # If ID not found
        print("Student ID not found.\n")


# Function to view student details by ID
def view_student():
    try:
        # Ask for student ID and convert to integer
        sid = int(input("Enter Student ID: "))
        # Call display function
        display_student(sid)
    except ValueError:
        # Handle non-integer input
        print("Invalid input.\n")


# Function to update a student's mobile number or class
def update_student():
    try:
        # Ask for student ID to update
        sid = int(input("Enter Student ID to update: "))
        # Get student record from dictionary
        student = students.get(sid)

        # Check if student exists
        if not student:
            print("Student not found.")
            return

        # Give update options
        print("1. Update Mobile")
        print("2. Update Class")

        # Get user's choice
        option = input("Choose option: ")

        # Update mobile number
        if option == '1':
            new_mobile = input("New Mobile (10 digits): ")
            if new_mobile.isdigit() and len(new_mobile) == 10:
                student["Mobile"] = new_mobile
                print("Mobile number updated.\n")
            else:
                print("Invalid mobile number.\n")

        # Update class
        elif option == '2':
            new_class = int(input("New Class (1–12): "))
            if 1 <= new_class <= 12:
                student["Class"] = new_class
                print("Class updated.\n")
            else:
                print("Invalid class.\n")

        # Handle invalid choice
        else:
            print("Invalid option.\n")

    except ValueError:
        # Handle invalid input
        print("Invalid input.\n")


# Function to remove a student record using ID
def remove_student():
    try:
        # Ask for student ID
        sid = int(input("Enter Student ID to remove: "))
        # Remove student if ID exists
        if sid in students:
            del students[sid]
            print("Student record removed.\n")
        else:
            print("Student not found.\n")
    except ValueError:
        # Handle invalid number input
        print("Invalid input.\n")


# Function to exit the program
def exit_system():
    # Print exit message and stop program
    print("Exiting system.")
    exit()


# Function to show main menu and handle user input
def main_menu():
    # Dictionary to map menu choices to functions
    options = {
        '1': new_admission,
        '2': view_student,
        '3': update_student,
        '4': remove_student,
        '5': exit_system
    }

    # Infinite loop to keep the system running
    while True:
        # Display main menu
        print("\n=== School Management System ===")
        print("1. New Admission")
        print("2. View Student Details")
        print("3. Update Student Info")
        print("4. Remove Student Record")
        print("5. Exit System")
        print("================================")

        # Get user's menu choice
        choice = input("Select option (1–5): ").strip()

        # Get function based on user choice
        action = options.get(choice)

        # Call function if valid choice
        if action:
            action()
        else:
            print("Invalid choice.\n")

        # Start the system
main_menu()
# This code implements a simple school management system that allows for student admissions,
# viewing, updating, and removing student records. It uses a dictionary to store student data.