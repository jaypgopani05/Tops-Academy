# # List of fixed time slots available each day
# time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]

# # Dictionary to store doctor schedules
# # Format: { "DoctorName": { "10am": [appointments], "11am": [], ... } }
# doctor_schedule = {}

# # List to store all patient appointments
# appointments = []


# # Function to book an appointment
# def book_appointment():
#     # Ask for patient name
#     name = input("Enter patient name: ").strip()

#     # Ask for age and validate input
#     try:
#         age = int(input("Enter age: "))
#     except ValueError:
#         print("Invalid age. Please enter a number.")
#         return

#     # Ask for mobile number and validate it
#     mobile = input("Enter mobile number (10 digits): ").strip()
#     if not mobile.isdigit() or len(mobile) != 10:
#         print("Invalid mobile number.")
#         return

#     # Ask for preferred doctor name
#     doctor = input("Enter preferred doctor's name: ").strip().title()

#     # If this doctor is new, initialize their schedule with empty slots
#     if doctor not in doctor_schedule:
#         doctor_schedule[doctor] = {slot: [] for slot in time_slots}

#     # Display available time slots with remaining seats
#     print("\nAvailable time slots for Dr. " + doctor + ":")
#     available = False  # Flag to check if any slot is available

#     for slot in time_slots:
#         remaining = 3 - len(doctor_schedule[doctor][slot])  # Each slot allows max 3 appointments
#         if remaining > 0:
#             print(f"{slot} - {remaining} slot(s) left")
#             available = True

#     if not available:
#         print("Sorry! No slots available for this doctor today.\n")
#         return

#     # Ask patient to choose a time slot
#     selected_slot = input("Enter preferred time slot (e.g., 10am): ").strip().lower()

#     # Validate chosen time slot
#     if selected_slot not in doctor_schedule[doctor]:
#         print("Invalid time slot selected.")
#         return

#     # Check if selected slot is full
#     if len(doctor_schedule[doctor][selected_slot]) >= 3:
#         print("Sorry, that slot is already full.\n")
#         return

#     # Create appointment record as a dictionary
#     appointment = {
#         "Name": name,
#         "Age": age,
#         "Mobile": mobile,
#         "Doctor": doctor,
#         "Slot": selected_slot
#     }

#     # Add appointment to doctor's schedule and global list
#     doctor_schedule[doctor][selected_slot].append(appointment)
#     appointments.append(appointment)

#     # Confirm booking
#     print("\nAppointment booked successfully!")
#     print("Patient Name:", name)
#     print("Doctor      :", doctor)
#     print("Time Slot   :", selected_slot)
#     print("----------------------------------\n")


# # Function to view appointment by mobile number
# def view_appointment():
#     # Ask for mobile number
#     mobile = input("Enter your mobile number to view appointment: ").strip()
#     found = False  # Flag to track if match is found

#     # Loop through all appointments to find a match
#     for appt in appointments:
#         if appt["Mobile"] == mobile:
#             # If match found, show details
#             print("\n--- Appointment Details ---")
#             print("Patient Name:", appt["Name"])
#             print("Age         :", appt["Age"])
#             print("Doctor      :", appt["Doctor"])
#             print("Time Slot   :", appt["Slot"])
#             print("----------------------------\n")
#             found = True

#     # If no match found, show message
#     if not found:
#         print("No appointment found with that mobile number.\n")


# # Function to cancel appointment by mobile number
# def cancel_appointment():
#     # Ask for mobile number
#     mobile = input("Enter your mobile number to cancel appointment: ").strip()
#     to_cancel = None  # Store the matching appointment

#     # Find the appointment in the list
#     for appt in appointments:
#         if appt["Mobile"] == mobile:
#             to_cancel = appt
#             break

#     # If no appointment is found
#     if not to_cancel:
#         print("No appointment found with that mobile number.\n")
#         return

#     # Remove appointment from global list
#     appointments.remove(to_cancel)

#     # Also remove from the doctor's schedule
#     doctor = to_cancel["Doctor"]
#     slot = to_cancel["Slot"]
#     doctor_schedule[doctor][slot].remove(to_cancel)

#     # Confirm cancellation
#     print("Appointment cancelled successfully.\n")


# # Function to display the main menu
# def main_menu():
#     while True:
#         # Display options
#         print("===== Clinic Appointment System =====")
#         print("1. Book Appointment")
#         print("2. View Appointment")
#         print("3. Cancel Appointment")
#         print("4. Exit")
#         print("=====================================")

#         # Get user choice
#         choice = input("Enter your choice (1-4): ").strip()

#         # Call functions based on choice
#         if choice == '1':
#             book_appointment()
#         elif choice == '2':
#             view_appointment()
#         elif choice == '3':
#             cancel_appointment()
#         elif choice == '4':
#             print("Exiting system. Take care!\n")
#             break
#         else:
#             print("Invalid choice. Please try again.\n")


# # Start the system by showing the menu
# main_menu()
# Hospital Management System Code Snippet
# =========================================================================================================
# Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assessment/Python files Assessment-1/Hospital_Management_System.py"
# ===== Clinic Appointment System =====
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# =====================================
# Enter your choice (1-4): 1
# Enter patient name: Jay Gopani
# Enter age: 30
# Enter mobile number (10 digits): 9409054326
# Enter preferred doctor's name: Dr. Devanshi Gopani

# Available time slots for Dr. Dr. Devanshi Gopani:
# 10am - 3 slot(s) left
# 11am - 3 slot(s) left
# 12pm - 3 slot(s) left
# 2pm - 3 slot(s) left
# 3pm - 3 slot(s) left
# Enter preferred time slot (e.g., 10am): 10am

# Appointment booked successfully!
# Patient Name: Jay Gopani
# Doctor      : Dr. Devanshi Gopani
# Time Slot   : 10am
# ----------------------------------

# ===== Clinic Appointment System =====
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# =====================================
# Enter your choice (1-4): 1
# Enter patient name: Janki Gopani
# Enter age: 27
# Enter mobile number (10 digits): 9712612595
# Enter preferred doctor's name: Dr. Devanshi Gopani

# Available time slots for Dr. Dr. Devanshi Gopani:
# 10am - 2 slot(s) left
# 11am - 3 slot(s) left
# 12pm - 3 slot(s) left
# 2pm - 3 slot(s) left
# 3pm - 3 slot(s) left
# Enter preferred time slot (e.g., 10am): 10am

# Appointment booked successfully!
# Patient Name: Janki Gopani
# Doctor      : Dr. Devanshi Gopani
# Time Slot   : 10am
# ----------------------------------

# ===== Clinic Appointment System =====
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# =====================================
# Enter your choice (1-4): 1
# Enter patient name: Jay Gopani
# Enter age: 30
# Enter mobile number (10 digits): 9409054326
# Enter preferred doctor's name: Dr. Devanshi Gopani

# Available time slots for Dr. Dr. Devanshi Gopani:
# 10am - 1 slot(s) left
# 11am - 3 slot(s) left
# 12pm - 3 slot(s) left
# 2pm - 3 slot(s) left
# 3pm - 3 slot(s) left
# Enter preferred time slot (e.g., 10am): 10am

# Appointment booked successfully!
# Patient Name: Jay Gopani
# Doctor      : Dr. Devanshi Gopani
# Time Slot   : 10am
# ----------------------------------

# ===== Clinic Appointment System =====
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# =====================================
# Enter your choice (1-4): 2
# Enter your mobile number to view appointment: 9409054326

# --- Appointment Details ---
# Patient Name: Jay Gopani
# Age         : 30
# Doctor      : Dr. Devanshi Gopani
# Time Slot   : 10am
# ----------------------------


# --- Appointment Details ---
# Patient Name: Jay Gopani
# Age         : 30
# Doctor      : Dr. Devanshi Gopani
# Time Slot   : 10am
# ----------------------------

# ===== Clinic Appointment System =====
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# =====================================
# Enter your choice (1-4): 2
# Enter your mobile number to view appointment: 9712612595

# --- Appointment Details ---
# Patient Name: Janki Gopani
# Age         : 27
# Doctor      : Dr. Devanshi Gopani
# Time Slot   : 10am
# ----------------------------

# ===== Clinic Appointment System =====
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# =====================================
# Enter your choice (1-4): 4         
# Exiting system. Take care!
# ======================================================================================
# ======================================================================================
# Need to update the code to handle duplicate appointments and ensure that each patient can only have one appointment per doctor per day.
# Need to ensure that the system does not allow multiple appointments for the same patient on the same day with the same doctor.
# This will require checking existing appointments before booking a new one.
# Asking for the patient's name and mobile number to check for existing appointments.
# ======================================================================================
# Dictionary to store appointments in memory
# Dictionary to store all appointments with a unique key
appointments = {}

# List of available doctors in the clinic
doctors = ["Dr. Devanshi Gopani", "Dr. Palak Shah", "Dr. Imran Bagwan"]

# List of available time slots for appointments
time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]

# Function to count how many appointments a doctor has at a given time
def get_appointments_by_doctor_time(doctor, time):
    count = 0  # Start count from 0
    for details in appointments.values():  # Loop through each appointment detail
        if details["Doctor"] == doctor and details["Time"] == time:  # If doctor and time match
            count += 1  # Increase count
    return count  # Return total count found

# Function to check if an exact appointment already exists (duplicate check)
def is_duplicate_appointment(name, age, mobile, doctor, time):
    for appt in appointments.values():  # Loop through existing appointments
        if (appt["Name"] == name and  # Compare name
            appt["Age"] == age and  # Compare age
            appt["Mobile"] == mobile and  # Compare mobile number
            appt["Doctor"] == doctor and  # Compare selected doctor
            appt["Time"] == time):  # Compare time slot
            return True  # Duplicate found
    return False  # No duplicate found

# Function to allow patient to book an appointment
def book_appointment():
    name = input("Enter Patient Name: ").strip()  # Take patient name input
    age = input("Enter Age: ").strip()  # Take patient age input
    mobile = input("Enter Mobile Number: ").strip()  # Take mobile number input

    # Check if mobile number is valid (must be 10 digits and numeric)
    if not (mobile.isdigit() and len(mobile) == 10):
        print("Invalid mobile number.")  # Show error if not valid
        return  # Stop function

    # Loop for doctor selection until valid input is given
    while True:
        print("Available Doctors:")  # Show list of doctors
        for idx, doc in enumerate(doctors, 1):  # Enumerate each doctor with index starting from 1
            print(f"{idx}. {doc}")  # Print doctor name

        try:
            doctor_index = int(input("Select doctor by number: "))  # Ask user to select doctor
            doctor = doctors[doctor_index - 1]  # Fetch doctor name based on index
            break  # Break loop if selection is valid
        except:
            print("Invalid doctor selection. Please try again.")  # Show error and retry

    # Loop for time slot selection until valid input is given
    while True:
        print("Available Time Slots:")  # Show list of time slots
        for idx, slot in enumerate(time_slots, 1):  # Enumerate each slot with index
            print(f"{idx}. {slot}")  # Print time slot

        try:
            time_index = int(input("Select time slot by number: "))  # Ask user to select slot
            time = time_slots[time_index - 1]  # Get time from list
            break  # Exit loop if selection is valid
        except:
            print("Invalid time slot selection. Please try again.")  # Show error and retry

    # Check if an appointment already exists with same details
    if is_duplicate_appointment(name, age, mobile, doctor, time):
        print("This appointment already exists with the same details.")  # Notify user

        # Ask user what they want to do next
        print("Choose an option:")
        print("1. Select a different time or update existing one")  # Option to select a new time
        print("2. Book for someone else")  # Option to book using other details

        choice = input("Enter your choice (1 or 2): ").strip()  # Take user choice input

        if choice == "1":
            # Loop again to select a new time
            while True:
                print("Re-select Available Time Slots:")  # Show time slots again
                for idx, slot in enumerate(time_slots, 1):  # Enumerate time slots
                    print(f"{idx}. {slot}")  # Show each option
                try:
                    time_index = int(input("Select new time slot by number: "))  # New selection
                    time = time_slots[time_index - 1]  # Get selected time
                    break  # Exit loop
                except:
                    print("Invalid time slot. Try again.")  # Show error
        elif choice == "2":
            print("Booking for someone else.")  # Show info
            return book_appointment()  # Restart the booking process
        else:
            print("Invalid choice. Returning to main menu.")  # Invalid input
            return  # Exit current function

    # Check if selected doctor is already fully booked at chosen time
    if get_appointments_by_doctor_time(doctor, time) >= 3:
        print("Selected doctor is fully booked at this time.")  # Show full booking message
        return  # Exit function

    # Create unique appointment ID using mobile number and time
    appointment_id = f"{mobile}_{time}"

    # Save all appointment details to the dictionary
    appointments[appointment_id] = {
        "Name": name,  # Save name
        "Age": age,  # Save age
        "Mobile": mobile,  # Save mobile number
        "Doctor": doctor,  # Save doctor
        "Time": time  # Save time slot
    }

    print("Appointment booked successfully.")  # Confirm booking to user

# Function to view appointment details using mobile number
def view_appointment():
    mobile = input("Enter your mobile number: ").strip()  # Ask for mobile number
    found = False  # Variable to track if any appointment is found

    # Loop through all saved appointments
    for appt_id, appt in appointments.items():
        if appt["Mobile"] == mobile:  # If mobile number matches
            found = True  # Mark as found
            print("\nAppointment Details:")  # Show details
            print(f"Patient Name: {appt['Name']}")  # Show name
            print(f"Age: {appt['Age']}")  # Show age
            print(f"Doctor: {appt['Doctor']}")  # Show doctor
            print(f"Time: {appt['Time']}")  # Show time
            print("-" * 25)  # Divider line

    if not found:
        print("No appointment found with this mobile number.")  # If no match found

# Function to cancel an appointment based on mobile number
def cancel_appointment():
    mobile = input("Enter your mobile number: ").strip()  # Ask for mobile number
    canceled = False  # Track if any cancellation was done

    # Find all appointment keys that match this mobile number
    to_delete = [key for key, appt in appointments.items() if appt["Mobile"] == mobile]

    # Loop through all keys found and delete them
    for key in to_delete:
        del appointments[key]  # Remove from dictionary
        canceled = True  # Mark cancellation

    if canceled:
        print("Appointment(s) cancelled successfully.")  # Show success message
    else:
        print("No appointment found with this mobile number.")  # No match found

# Function to display and handle main menu of the system
def main_menu():
    while True:  # Infinite loop until user exits
        print("\nClinic Appointment System")  # Title
        print("1. Book Appointment")  # Menu option 1
        print("2. View Appointment")  # Menu option 2
        print("3. Cancel Appointment")  # Menu option 3
        print("4. Exit")  # Menu option 4

        choice = input("Select option (1–4): ").strip()  # Take user input

        if choice == "1":
            book_appointment()  # Call booking function
        elif choice == "2":
            view_appointment()  # Call view function
        elif choice == "3":
            cancel_appointment()  # Call cancel function
        elif choice == "4":
            print("Exiting system.")  # Exit message
            break  # Exit loop
        else:
            print("Invalid option. Try again.")  # If input is wrong

# Start the application by calling main menu
main_menu()
# Hospital Management System Code Snippet
# =========================================================================================================