import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

# =========================
# Tkinter Root
# =========================
root = tk.Tk()
root.title("SQL Playground - Multi-Database")
root.geometry("1300x750")

# =========================
# Database Connection
# =========================
conn = sqlite3.connect("multi_db_playground.db")
cursor = conn.cursor()

# =========================
# Database Templates
# =========================
# Define tables and their columns per database type
db_templates = {
    "Organization": {
        "tables": {
            "Departments": [("DeptID","INTEGER"),("DeptName","TEXT"),("Location","TEXT")],
            "Employees": [("EmpID","INTEGER"),("FirstName","TEXT"),("LastName","TEXT"),("DeptID","INTEGER")],
            "Salaries": [("EmpID","INTEGER"),("SalaryAmount","REAL")],
            "Projects": [("ProjectID","INTEGER"),("ProjectName","TEXT")],
            "EmployeeProjects": [("EmpID","INTEGER"),("ProjectID","INTEGER")]
        }
    },
    "Students": {
        "tables": {
            "Students": [("StudentID","INTEGER"),("FirstName","TEXT"),("LastName","TEXT"),("Age","INTEGER")],
            "Courses": [("CourseID","INTEGER"),("CourseName","TEXT"),("Credits","INTEGER")],
            "Enrollments": [("StudentID","INTEGER"),("CourseID","INTEGER"),("Grade","TEXT")]
        }
    },
    "Inventory": {
        "tables": {
            "Products": [("ProductID","INTEGER"),("ProductName","TEXT"),("Price","REAL")],
            "Suppliers": [("SupplierID","INTEGER"),("SupplierName","TEXT"),("Contact","TEXT")],
            "Orders": [("OrderID","INTEGER"),("ProductID","INTEGER"),("SupplierID","INTEGER"),("OrderQty","INTEGER")]
        }
    }
}

# =========================
# Current DB Type
# =========================
db_type_var = tk.StringVar(value="Organization")

# =========================
# Initialize Tables
# =========================
def create_tables(db_type):
    for table_name, columns in db_templates[db_type]["tables"].items():
        col_defs = ", ".join([f"{col[0]} {col[1]}" + (" PRIMARY KEY AUTOINCREMENT" if col[0].endswith("ID") else "") for col in columns])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({col_defs})")
    conn.commit()

# =========================
# Add Random Data
# =========================
def add_random_data():
    db_type = db_type_var.get()
    tables = db_templates[db_type]["tables"]

    for _ in range(50):  # Add 50 records
        if db_type == "Organization":
            # Departments
            cursor.execute("INSERT OR IGNORE INTO Departments (DeptName, Location) VALUES (?,?)",
                           (f"Dept{random.randint(1,20)}", f"City{random.randint(1,20)}"))
            # Employees
            dept_count = cursor.execute("SELECT COUNT(*) FROM Departments").fetchone()[0]
            cursor.execute("INSERT INTO Employees (FirstName, LastName, DeptID) VALUES (?,?,?)",
                           (f"FName{random.randint(1,500)}", f"LName{random.randint(1,500)}", random.randint(1, dept_count)))
            emp_id = cursor.lastrowid
            # Salaries
            cursor.execute("INSERT INTO Salaries (EmpID, SalaryAmount) VALUES (?,?)",
                           (emp_id, random.randint(40000,150000)))
            # Projects
            cursor.execute("INSERT INTO Projects (ProjectName) VALUES (?)",
                           (f"Project{random.randint(1,500)}",))
            project_id = cursor.lastrowid
            cursor.execute("INSERT OR IGNORE INTO EmployeeProjects (EmpID, ProjectID) VALUES (?,?)",
                           (emp_id, project_id))

        elif db_type == "Students":
            cursor.execute("INSERT INTO Students (FirstName, LastName, Age) VALUES (?,?,?)",
                           (f"FName{random.randint(1,500)}", f"LName{random.randint(1,500)}", random.randint(15,30)))
            student_id = cursor.lastrowid
            cursor.execute("INSERT OR IGNORE INTO Courses (CourseName, Credits) VALUES (?,?)",
                           (f"Course{random.randint(1,50)}", random.randint(1,5)))
            course_id = cursor.lastrowid
            cursor.execute("INSERT INTO Enrollments (StudentID, CourseID, Grade) VALUES (?,?,?)",
                           (student_id, course_id, random.choice(["A","B","C","D"])))

        elif db_type == "Inventory":
            cursor.execute("INSERT INTO Products (ProductName, Price) VALUES (?,?)",
                           (f"Product{random.randint(1,500)}", random.randint(10,500)))
            product_id = cursor.lastrowid
            cursor.execute("INSERT OR IGNORE INTO Suppliers (SupplierName, Contact) VALUES (?,?)",
                           (f"Supplier{random.randint(1,50)}", f"Contact{random.randint(1000,9999)}"))
            supplier_id = cursor.lastrowid
            cursor.execute("INSERT INTO Orders (ProductID, SupplierID, OrderQty) VALUES (?,?,?)",
                           (product_id, supplier_id, random.randint(1,100)))

    conn.commit()
    messagebox.showinfo("Success", "50 random records added to the selected database!")

# =========================
# View Table Data
# =========================
def view_table_data(table_name, treeview):
    if not table_name:
        messagebox.showerror("Error","Select a table first")
        return
    # Clear tree
    for i in treeview.get_children():
        treeview.delete(i)
    cursor.execute(f"PRAGMA table_info({table_name})")
    cols = [c[1] for c in cursor.fetchall()]
    treeview["columns"] = cols
    treeview["show"] = "headings"
    for col in cols:
        treeview.heading(col, text=col)
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        treeview.insert("",tk.END,values=row)

# =========================
# Help / Cheat Sheet
# =========================
def show_help():
    help_win = tk.Toplevel()
    help_win.title("SQL Help / Cheat Sheet")
    help_win.geometry("1000x600")
    text_area = scrolledtext.ScrolledText(help_win, width=120, height=35)
    text_area.pack(padx=5,pady=5)

    db_type = db_type_var.get()
    tables = db_templates[db_type]["tables"]

    help_text = f"===== SQL Cheat Sheet for {db_type} =====\n\n"

    help_text += "-- DDL Commands --\n"
    for t in tables:
        help_text += f"CREATE TABLE {t}(...);\n"
    help_text += "ALTER TABLE table_name ADD COLUMN col_name TYPE;\nDROP TABLE table_name;\n\n"

    help_text += "-- SELECT Queries --\n"
    for t in tables:
        help_text += f"SELECT * FROM {t};\nSELECT COUNT(*) FROM {t};\nSELECT * FROM {t} ORDER BY ROWID DESC;\n"

    help_text += "\n-- INSERT Queries --\n"
    for t, cols in tables.items():
        col_names = ", ".join([c[0] for c in cols])
        vals = ", ".join(["'example'" if "TEXT" in c[1] else "100" for c in cols])
        help_text += f"INSERT INTO {t} ({col_names}) VALUES ({vals});\n"

    help_text += "\n-- UPDATE Queries --\n"
    for t, cols in tables.items():
        help_text += f"UPDATE {t} SET {cols[0][0]}='UpdatedValue' WHERE ROWID=1;\n"

    help_text += "\n-- DELETE Queries --\n"
    for t in tables:
        help_text += f"DELETE FROM {t} WHERE ROWID=1;\n"

    help_text += "\n-- JOIN / Aggregates / Subqueries Examples --\n"
    if db_type=="Organization":
        help_text += "SELECT e.FirstName, s.SalaryAmount FROM Employees e INNER JOIN Salaries s ON e.EmpID=s.EmpID;\n"
        help_text += "SELECT e.FirstName, p.ProjectName FROM Employees e INNER JOIN EmployeeProjects ep ON e.EmpID=ep.EmpID INNER JOIN Projects p ON ep.ProjectID=p.ProjectID;\n"
    elif db_type=="Students":
        help_text += "SELECT s.FirstName, c.CourseName FROM Students s INNER JOIN Enrollments e ON s.StudentID=e.StudentID INNER JOIN Courses c ON e.CourseID=c.CourseID;\n"
    elif db_type=="Inventory":
        help_text += "SELECT p.ProductName, o.OrderQty, s.SupplierName FROM Products p INNER JOIN Orders o ON p.ProductID=o.ProductID INNER JOIN Suppliers s ON o.SupplierID=s.SupplierID;\n"

    text_area.insert(tk.END, help_text)
    text_area.config(state="disabled")

# =========================
# Tkinter Main GUI
# =========================
# Top Frame: Database Selection
top_frame = ttk.Frame(root)
top_frame.pack(fill="x", padx=5, pady=5)
ttk.Label(top_frame, text="Select Database Type:").pack(side="left", padx=5)
db_menu = ttk.Combobox(top_frame, textvariable=db_type_var, values=list(db_templates.keys()))
db_menu.pack(side="left", padx=5)
ttk.Button(top_frame, text="Init Tables", command=lambda:create_tables(db_type_var.get())).pack(side="left", padx=5)

# Buttons Frame
btn_frame = ttk.Frame(root)
btn_frame.pack(padx=5,pady=5)

# Treeview
result_tree = ttk.Treeview(root)
result_tree.pack(fill="both", expand=True, padx=5, pady=5)

# Buttons
ttk.Button(btn_frame, text="View Table", command=lambda: view_table_data(db_menu.get(), result_tree)).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Add Random Data", command=add_random_data).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Help / Cheat Sheet", command=show_help).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Exit", command=root.destroy).pack(side="left", padx=5)

root.mainloop()
# =========================