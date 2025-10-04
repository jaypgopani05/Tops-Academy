import sqlite3                          # For SQLite database operations
import pandas as pd                     # For data display and DataFrame operations
from datetime import datetime           # To capture current date and time
from email.message import EmailMessage  # For sending OTP emails
import smtplib                           # For sending emails
import random                            # To generate OTPs and random values
from aiosmtpd.controller import Controller  # Local SMTP server for debugging emails
import asyncio                           # For asynchronous email handling

# ==========================
# Local SMTP Debug Server
# ==========================
class PrintHandler:
    # Handles incoming emails and prints them to console
    async def handle_DATA(self, server, session, envelope):
        print("\n----- New Email Received -----")
        print(envelope.content.decode('utf8', errors='replace'))  # Print email content
        print("------------------------------\n")
        return '250 OK'

# Start the SMTP server on localhost port 1025
controller = Controller(PrintHandler(), hostname='localhost', port=1025)
controller.start()
print("Local SMTP server started on localhost:1025")

# ==========================
# Database Setup
# ==========================
# Connect or create the main database
conn = sqlite3.connect("employee_management.db")
cur = conn.cursor()

# Create admin table to store admin details
cur.execute("""CREATE TABLE IF NOT EXISTS admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
            )""")

# Create employees table with Employee ID, role, password, verification status
cur.execute("""CREATE TABLE IF NOT EXISTS employees (
                emp_id TEXT PRIMARY KEY,
                name TEXT,
                department TEXT,
                role TEXT,
                password TEXT,
                verified TEXT
            )""")

# Create attendance table to store daily punches
cur.execute("""CREATE TABLE IF NOT EXISTS attendance (
                emp_id TEXT,
                name TEXT,
                date TEXT,
                time TEXT
            )""")

# Table to maintain Employee ID counters for each pretext
cur.execute("""CREATE TABLE IF NOT EXISTS id_counters (
                pretext TEXT PRIMARY KEY,
                counter INTEGER
            )""")
conn.commit()

# ==========================
# Helper Functions
# ==========================
def send_otp(recipient_email):
    """
    Sends OTP to given email via local SMTP server.
    Returns the OTP for verification.
    """
    otp = str(random.randint(100000, 999999))  # Generate 6-digit OTP
    msg = EmailMessage()                        # Create email message
    msg['Subject'] = "Your OTP Code"
    msg['From'] = "admin@company.com"
    msg['To'] = recipient_email
    msg.set_content(f"Your OTP is: {otp}")
    
    # Send via local SMTP server
    with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.send_message(msg)
    
    print(f"OTP sent to {recipient_email}. Check console output for email content.")
    return otp

def admin_exists():
    """
    Checks if admin is already registered.
    Returns True if exists, else False.
    """
    cur.execute("SELECT * FROM admin")
    return cur.fetchone() is not None

def register_admin():
    """
    Registers admin with OTP verification.
    """
    name = input("Enter Admin Name: ").strip()
    email = input("Enter Admin Email: ").strip()
    otp = send_otp(email)
    user_otp = input("Enter OTP sent to your email: ").strip()
    if user_otp == otp:
        cur.execute("INSERT INTO admin (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("Admin registered successfully!")
    else:
        print("Invalid OTP. Registration failed.")

def generate_emp_id(department, role):
    """
    Generates Employee ID based on department and role with sequential counter.
    """
    pretext = ""
    # Employee IDs for normal employees
    if role.upper() == "EMPLOYEE":
        if department.upper() == "IT SECURITY":
            pretext = "ITSM"
        elif department.upper() == "ACCOUNTING":
            pretext = "ACC"
        elif department.upper() == "DATA ANALYTICS":
            pretext = "DA"
        elif department.upper() == "DATA SCIENCE":
            pretext = "DS"
        elif department.upper() == "SUPPORT SERVICE":
            pretext = "SSP"
    # Team Leads
    elif role.upper() == "TL":
        if department.upper() == "IT SECURITY":
            pretext = "TLITSM"
        elif department.upper() == "DATA ANALYTICS":
            pretext = "TLDA"
        elif department.upper() == "DATA SCIENCE":
            pretext = "TLDS"
    # Managers
    elif role.upper() == "MANAGER":
        if department.upper() == "IT SECURITY":
            pretext = "MGITSM"
        elif department.upper() == "DATA ANALYTICS":
            pretext = "MGDA"
        elif department.upper() == "DATA SCIENCE":
            pretext = "MGDS"
    else:
        pretext = "GEN"

    # Retrieve current counter for the pretext
    cur.execute("SELECT counter FROM id_counters WHERE pretext=?", (pretext,))
    row = cur.fetchone()
    if row:
        counter = row[0] + 1
        cur.execute("UPDATE id_counters SET counter=? WHERE pretext=?", (counter, pretext))
    else:
        counter = 1
        cur.execute("INSERT INTO id_counters (pretext, counter) VALUES (?,?)", (pretext, counter))
    conn.commit()
    # Format Employee ID with 3 digits
    emp_id = f"{pretext}{str(counter).zfill(3)}"
    return emp_id

def register_user():
    """
    Registers normal user (employee/TL/Manager) pending admin approval.
    """
    name = input("Enter Name: ").strip()
    dept = input("Enter Department (IT Security / Accounting / Data Analytics / Data Science / Support Service): ").strip()
    role = input("Enter Role (Employee / TL / Manager): ").strip()
    emp_id = generate_emp_id(dept, role)
    password = input("Set your password: ").strip()
    # Insert with verified status N (pending)
    cur.execute("INSERT INTO employees (emp_id, name, department, role, password, verified) VALUES (?,?,?,?,?,?)",
                (emp_id, name, dept, role.upper(), password, "N"))
    conn.commit()
    print(f"Registration submitted. Employee ID: {emp_id}. Awaiting admin approval.")

def approve_users():
    """
    Admin approves pending users.
    """
    df = pd.read_sql("SELECT * FROM employees WHERE verified='N'", conn)
    if df.empty:
        print("No pending users.")
        return
    print("\n=== Pending Users ===")
    print(df.to_string(index=False))
    emp_id = input("Enter Employee ID to approve: ").strip()
    cur.execute("UPDATE employees SET verified='Y' WHERE emp_id=?", (emp_id,))
    conn.commit()
    print(f"Employee {emp_id} approved successfully.")

def add_employee():
    """
    Admin adds new employee/TL/Manager directly as verified user.
    """
    name = input("Enter Employee Name: ").strip()
    dept = input("Enter Department: ").strip()
    role = input("Enter Role (Employee / TL / Manager): ").strip()
    emp_id = generate_emp_id(dept, role)
    password = input("Set a password for this Employee: ").strip()
    cur.execute("INSERT INTO employees (emp_id, name, department, role, password, verified) VALUES (?,?,?,?,?,?)",
                (emp_id, name, dept, role.upper(), password, "Y"))
    conn.commit()
    print(f"Employee registered successfully! Employee ID: {emp_id}")

def view_employees():
    """
    Display all employees with details.
    """
    df = pd.read_sql("SELECT * FROM employees", conn)
    if df.empty:
        print("No employees found.")
    else:
        print("\n=== Employees ===")
        print(df)

def punch_attendance():
    """
    Punch attendance only if employee is verified and password is correct.
    """
    emp_id = input("Enter Employee ID: ").strip()
    password = input("Enter Password: ").strip()
    cur.execute("SELECT name FROM employees WHERE emp_id=? AND password=? AND verified='Y'", (emp_id, password))
    row = cur.fetchone()
    if row:
        name = row[0]
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        cur.execute("INSERT INTO attendance VALUES (?,?,?,?)", (emp_id, name, date, time))
        conn.commit()
        print("Attendance recorded successfully!")
    else:
        print("Invalid credentials or not verified by admin!")

def view_attendance():
    """
    View all attendance logs.
    """
    df = pd.read_sql("SELECT * FROM attendance", conn)
    if df.empty:
        print("No attendance records found.")
    else:
        print("\n=== Attendance Logs ===")
        print(df)

# ==========================
# Main Menu
# ==========================
def main_menu():
    while True:
        print("\n===== Employee Management & Attendance System =====")
        print("1. Register Admin (first time only)")
        print("2. Add Employee / TL / Manager (Admin only)")
        print("3. View Employees")
        print("4. Punch Attendance")
        print("5. View Attendance Logs")
        print("6. Exit")
        print("7. Register as Normal User")
        print("8. Approve Pending Users (Admin only)")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            if admin_exists():
                print("Admin already exists.")
            else:
                register_admin()
        elif choice == '2':
            if not admin_exists():
                print("No admin registered yet.")
            else:
                add_employee()
        elif choice == '3':
            view_employees()
        elif choice == '4':
            punch_attendance()
        elif choice == '5':
            view_attendance()
        elif choice == '6':
            print("Exiting... All data saved.")
            break
        elif choice == '7':
            register_user()
        elif choice == '8':
            if not admin_exists():
                print("No admin registered yet.")
            else:
                approve_users()
        else:
            print("Invalid choice. Enter 1-8.")

# Run main menu11

main_menu()
