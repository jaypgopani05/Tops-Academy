import sqlite3  # Importing sqlite3 to work with the SQLite database
import pandas as pd  # Importing pandas to handle dataframes and Excel operations
import os  # Importing os to check if files exist before using them

# Connect to a persistent database file (employees.db) so data is saved permanently
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()  # Create a cursor to execute SQL commands

# Create employees table if it does not exist already
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary REAL
)
""")
conn.commit()  # Save the table creation if new

# Function to add an employee
def add_employee():
    name = input("Enter Name: ")  # Get employee name
    dept = input("Enter Department: ")  # Get employee department
    salary = float(input("Enter Salary: "))  # Get employee salary
    # Insert the record into the employees table
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", 
                   (name, dept, salary))
    conn.commit()  # Save the insertion
    print("Employee added successfully!")

# Function to view all employees
def view_employees():
    df = pd.read_sql("SELECT * FROM employees", conn)  # Fetch all employee records into dataframe
    print(df.to_string(index=False))  # Print the dataframe without index

# Function to update employee details
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))  # Ask which employee ID to update
    name = input("Enter New Name: ")  # Ask for updated name
    dept = input("Enter New Department: ")  # Ask for updated department
    salary = float(input("Enter New Salary: "))  # Ask for updated salary
    # Update record in database
    cursor.execute("UPDATE employees SET name=?, department=?, salary=? WHERE id=?", 
                   (name, dept, salary, emp_id))
    conn.commit()  # Save the update
    print("Employee updated successfully!")

# Function to delete an employee
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))  # Ask which employee ID to delete
    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))  # Delete that employee
    conn.commit()  # Save the deletion
    print("Employee deleted successfully!")

# Function to search employees
def search_employee():
    keyword = input("Enter search keyword (name or department): ")  # Ask user what to search
    # Fetch matching records
    query = "SELECT * FROM employees WHERE name LIKE ? OR department LIKE ?"
    df = pd.read_sql(query, conn, params=(f"%{keyword}%", f"%{keyword}%"))
    print(df.to_string(index=False))  # Print search results

# Function to export employees to Excel
def export_to_excel():
    df = pd.read_sql("SELECT * FROM employees", conn)  # Read all data into dataframe
    file_name = "employees_export.xlsx"  # Output Excel file name
    df.to_excel(file_name, index=False)  # Save dataframe to Excel file
    print(f"Data exported to {file_name}")

# Function to import employees from Excel
def import_from_excel():
    file_path = input("Enter the Excel file path: ")  # Ask user for Excel file path
    if os.path.exists(file_path):  # Check if the file actually exists
        df = pd.read_excel(file_path)  # Read data from Excel file
        df.to_sql("employees", conn, if_exists="append", index=False)  # Append to database
        conn.commit()  # Save changes
        print("Data imported from Excel successfully!")
    else:
        print("File not found. Please enter a valid file path.")

# Menu-driven system
while True:
    # Display menu options
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Export to Excel")
    print("7. Import from Excel")
    print("8. Exit")

    choice = input("Enter your choice: ")  # Ask user to select an option

    # Call corresponding function based on choice
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        search_employee()
    elif choice == "6":
        export_to_excel()
    elif choice == "7":
        import_from_excel()
    elif choice == "8":
        print("Exiting... Goodbye!")  # Exit message
        break
    else:
        print("Invalid choice! Please try again.")  # Handle wrong input
