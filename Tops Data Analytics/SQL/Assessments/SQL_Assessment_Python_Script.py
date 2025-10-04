import mysql.connector  # Import the MySQL connector library to interact with MySQL
from mysql.connector import errorcode  # Import error codes for exception handling

# ===============================
# 1. MySQL connection details
# ===============================
DB_HOST = "localhost"        # Hostname where MySQL server is running
DB_USER = "root"             # MySQL username
DB_PASSWORD = "Mysql@2026"  # MySQL password; replace with your own
DB_NAME = "try"              # Name of the database we will create

try:
    # Connect to MySQL server (without specifying database yet)
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()  # Create a cursor object to execute SQL queries
    print("Connected to MySQL server")

    # ===============================
    # 2. Create Database
    # ===============================
    cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")  # Drop database if it exists
    cursor.execute(f"CREATE DATABASE {DB_NAME}")          # Create a new database
    cursor.execute(f"USE {DB_NAME}")                     # Select the database for use
    print(f"Database '{DB_NAME}' created and selected")

    # ===============================
    # 3. Create Tables
    # ===============================
    # Create 'employees' table
    cursor.execute("""
    CREATE TABLE employees (
        Employee_id INT AUTO_INCREMENT PRIMARY KEY,  # Primary key with auto increment
        name VARCHAR(100),                           # Employee name
        position VARCHAR(100),                       # Job position
        salary DECIMAL(10, 2),                       # Salary with 2 decimal places
        hire_date DATE                               # Date when employee was hired
    )
    """)

    # Create 'employee_audit' table to log changes
    cursor.execute("""
    CREATE TABLE employee_audit (
        audit_id INT AUTO_INCREMENT PRIMARY KEY,     # Primary key for audit table
        employee_id INT,                             # ID of employee being logged
        name VARCHAR(100),                           # Employee name
        position VARCHAR(100),                       # Job position
        salary DECIMAL(10, 2),                       # Salary
        hire_date DATE,                              # Hire date
        action_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  # When the action occurred
        action_type VARCHAR(20),                     # Type of action: INSERT, UPDATE, DELETE
        action_user VARCHAR(100)                     # User who performed the action
    )
    """)
    print("Tables 'employees' and 'employee_audit' created")

    # ===============================
    # 4. Create Triggers
    # ===============================
    # List of triggers to create: name, action type, reference for OLD/NEW
    triggers = [
        ("after_employee_insert", "INSERT", "NEW"),
        ("after_employee_update", "UPDATE", "OLD"),
        ("after_employee_delete", "DELETE", "OLD")
    ]

    for trg_name, action, ref in triggers:
        cursor.execute(f"DROP TRIGGER IF EXISTS {trg_name}")  # Drop trigger if it exists
        # Create trigger SQL
        trigger_sql = f"""
        CREATE TRIGGER {trg_name}
        AFTER {action} ON employees
        FOR EACH ROW
        BEGIN
            INSERT INTO employee_audit 
            (employee_id, name, position, salary, hire_date, action_type, action_user)
            VALUES ({ref}.Employee_id, {ref}.name, {ref}.position, {ref}.salary, {ref}.hire_date, '{action}', CURRENT_USER());
        END
        """
        cursor.execute(trigger_sql)  # Execute trigger creation
    print("Triggers for INSERT, UPDATE, DELETE created")

    # ===============================
    # 5. Create Stored Procedure
    # ===============================
    cursor.execute("DROP PROCEDURE IF EXISTS AddEmployee")  # Drop if procedure already exists
    sp_sql = f"""
    CREATE PROCEDURE AddEmployee (
        IN p_name VARCHAR(100),
        IN p_position VARCHAR(100),
        IN p_salary DECIMAL(10,2),
        IN p_hire_date DATE
    )
    BEGIN
        INSERT INTO employees (name, position, salary, hire_date)
        VALUES (p_name, p_position, p_salary, p_hire_date);
    END
    """
    cursor.execute(sp_sql)  # Create the procedure
    print("Stored procedure 'AddEmployee' created")

    # ===============================
    # 6. Test Inserts, Updates, Deletes
    # ===============================
    # Insert sample employees using stored procedure
    cursor.callproc("AddEmployee", ("John Doe", "Software Engineer", 80000, "2022-01-15"))
    cursor.callproc("AddEmployee", ("Jane Smith", "Project Manager", 90000, "2021-05-22"))
    cursor.callproc("AddEmployee", ("Alice Johnson", "UX Designer", 75000, "2023-03-01"))

    # Update salary for one employee
    cursor.execute("UPDATE employees SET salary = 95000 WHERE name = 'Jane Smith'")

    # Delete an employee
    cursor.execute("DELETE FROM employees WHERE name = 'Alice Johnson'")

    conn.commit()  # Commit all changes to the database
    print("Sample data inserted, updated, and deleted")

    # ===============================
    # 7. Show Audit Log
    # ===============================
    # Retrieve and display audit log
    cursor.execute("""
        SELECT audit_id, employee_id, name, action_type, action_user, action_date 
        FROM employee_audit
        ORDER BY audit_id
    """)
    rows = cursor.fetchall()  # Fetch all results
    print("\n===== Employee Audit Log =====")
    for row in rows:
        print(row)  # Print each row of audit log

# ===============================
# Exception Handling
# ===============================
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(f"Database {DB_NAME} does not exist")
    else:
        print(err)

# ===============================
# Cleanup
# ===============================
finally:
    if 'cursor' in locals():  # Close cursor if it exists
        cursor.close()
    if 'conn' in locals() and conn.is_connected():  # Close connection if it exists and open
        conn.close()
        print("MySQL connection closed")
        