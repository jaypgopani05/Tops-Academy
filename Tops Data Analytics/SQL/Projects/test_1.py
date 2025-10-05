import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import random
import string
import re

# =========================
# Tkinter Root
# =========================
root = tk.Tk()
root.title("SQL Playground - Multi-Database + Custom DB Creator")
root.geometry("1400x820")

# =========================
# Database Connection
# =========================
conn = sqlite3.connect("multi_db_playground.db")
cursor = conn.cursor()

# =========================
# Utility: sanitize identifiers and quoting
# =========================
IDENT_RE = re.compile(r'[^A-Za-z0-9_]')

def sanitize_identifier(name: str) -> str:
    if not name:
        raise ValueError("Empty identifier")
    s = IDENT_RE.sub("_", name.strip())
    if s[0].isdigit():
        s = "_" + s
    return s

def quoted(name: str) -> str:
    s = sanitize_identifier(name)
    return f'"{s}"'

# =========================
# Database Templates (predefined)
# =========================
db_templates = {
    "Organization": {
        "tables": {
            "Departments": [("DeptID", "INTEGER"), ("DeptName", "TEXT"), ("Location", "TEXT")],
            "Employees": [("EmpID", "INTEGER"), ("FirstName", "TEXT"), ("LastName", "TEXT"), ("DeptID", "INTEGER")],
            "Salaries": [("EmpID", "INTEGER"), ("SalaryAmount", "REAL")],
            "Projects": [("ProjectID", "INTEGER"), ("ProjectName", "TEXT")],
            "EmployeeProjects": [("EmpID", "INTEGER"), ("ProjectID", "INTEGER")]
        }
    },
    "Students": {
        "tables": {
            "Students": [("StudentID", "INTEGER"), ("FirstName", "TEXT"), ("LastName", "TEXT"), ("Age", "INTEGER")],
            "Courses": [("CourseID", "INTEGER"), ("CourseName", "TEXT"), ("Credits", "INTEGER")],
            "Enrollments": [("StudentID", "INTEGER"), ("CourseID", "INTEGER"), ("Grade", "TEXT")]
        }
    },
    "Inventory": {
        "tables": {
            "Products": [("ProductID", "INTEGER"), ("ProductName", "TEXT"), ("Price", "REAL")],
            "Suppliers": [("SupplierID", "INTEGER"), ("SupplierName", "TEXT"), ("Contact", "TEXT")],
            "Orders": [("OrderID", "INTEGER"), ("ProductID", "INTEGER"), ("SupplierID", "INTEGER"), ("OrderQty", "INTEGER")]
        }
    }
}

# =========================
# UI Variables
# =========================
db_type_var = tk.StringVar(value="Organization")
current_table = tk.StringVar()

# =========================
# Random Data Generators
# =========================
def random_text(prefix="Txt", length=6):
    return f"{prefix}_{''.join(random.choices(string.ascii_lowercase, k=length))}"

def random_int(low=1, high=100):
    return random.randint(low, high)

def random_real(low=1.0, high=1000.0):
    return round(random.uniform(low, high), 2)

# =========================
# Create Tables
# =========================
def create_tables(db_type):
    if db_type not in db_templates:
        messagebox.showerror("Error", f"Unknown DB type: {db_type}")
        return
    tables = db_templates[db_type]["tables"]
    for raw_table_name, cols in tables.items():
        tbl = sanitize_identifier(raw_table_name)
        col_defs_list = []
        for col_name, col_type in cols:
            c = sanitize_identifier(col_name)
            t = col_type.strip().upper()
            if c.upper().endswith("ID") and "INT" in t:
                col_def = f'{quoted(c)} INTEGER PRIMARY KEY AUTOINCREMENT'
            else:
                col_def = f'{quoted(c)} {t}'
            col_defs_list.append(col_def)
        col_defs = ", ".join(col_defs_list)
        sql = f'CREATE TABLE IF NOT EXISTS {quoted(tbl)} ({col_defs})'
        cursor.execute(sql)
    conn.commit()
    update_table_menu_values(db_type)

# =========================
# Update Table Combobox
# =========================
def update_table_menu_values(selected_db=None):
    sel = selected_db or db_type_var.get()
    if sel not in db_templates:
        table_menu["values"] = []
        current_table.set("")
        return
    tables = list(db_templates[sel]["tables"].keys())
    table_menu["values"] = tables
    if tables:
        current_table.set(tables[0])
    else:
        current_table.set("")

# =========================
# Add Random Data
# =========================
def add_random_data():
    db_type = db_type_var.get()
    if db_type not in db_templates:
        messagebox.showerror("Error", "Select a valid database type first.")
        return
    create_tables(db_type)

    # Organization logic
    if db_type == "Organization":
        cursor.execute(f"SELECT COUNT(*) FROM {quoted('Departments')}")
        deps = cursor.fetchone()[0]
        if deps == 0:
            depts = ["HR","Finance","IT","Marketing","Sales","Admin","Legal","Operations","R&D","Support"]
            for d in depts:
                cursor.execute(f"INSERT INTO {quoted('Departments')} (DeptName,Location) VALUES (?,?)", (d, random_text("City",4)))
            conn.commit()
        for _ in range(50):
            dept_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted('Departments')}").fetchone()[0] or 1
            first = random_text("F",5).capitalize()
            last = random_text("L",6).capitalize()
            dept_id = random_int(1, dept_count)
            cursor.execute(f"INSERT INTO {quoted('Employees')} (FirstName,LastName,DeptID) VALUES (?,?,?)", (first,last,dept_id))
            emp_id = cursor.lastrowid
            cursor.execute(f"INSERT INTO {quoted('Salaries')} (EmpID,SalaryAmount) VALUES (?,?)", (emp_id, random_int(40000,150000)))
            cursor.execute(f"INSERT INTO {quoted('Projects')} (ProjectName) VALUES (?)", (random_text("Project",5),))
            project_id = cursor.lastrowid
            cursor.execute(f"INSERT OR IGNORE INTO {quoted('EmployeeProjects')} (EmpID,ProjectID) VALUES (?,?)", (emp_id, project_id))

    # Students logic
    elif db_type == "Students":
        cursor.execute(f"SELECT COUNT(*) FROM {quoted('Courses')}")
        course_count = cursor.fetchone()[0]
        if course_count == 0:
            for s in ["Math","Physics","Chemistry","History","English"]:
                cursor.execute(f"INSERT INTO {quoted('Courses')} (CourseName,Credits) VALUES (?,?)", (s, random_int(2,5)))
            conn.commit()
        for _ in range(50):
            first = random_text("S",5).capitalize()
            last = random_text("S",6).capitalize()
            age = random_int(15,30)
            cursor.execute(f"INSERT INTO {quoted('Students')} (FirstName,LastName,Age) VALUES (?,?,?)", (first,last,age))
            student_id = cursor.lastrowid
            course_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted('Courses')}").fetchone()[0] or 1
            course_id = random_int(1, course_count)
            cursor.execute(f"INSERT INTO {quoted('Enrollments')} (StudentID,CourseID,Grade) VALUES (?,?,?)", (student_id,course_id,random.choice(["A","B","C","D"])))

    # Inventory logic
    elif db_type == "Inventory":
        cursor.execute(f"SELECT COUNT(*) FROM {quoted('Suppliers')}")
        sup_count = cursor.fetchone()[0]
        if sup_count == 0:
            for i in range(5):
                cursor.execute(f"INSERT INTO {quoted('Suppliers')} (SupplierName,Contact) VALUES (?,?)", (random_text("Supplier",4), random_text("Phone",6)))
            conn.commit()
        for _ in range(50):
            product = random_text("Prod",5)
            price = random_real(10,500)
            cursor.execute(f"INSERT INTO {quoted('Products')} (ProductName,Price) VALUES (?,?)", (product, price))
            product_id = cursor.lastrowid
            supplier_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted('Suppliers')}").fetchone()[0] or 1
            supplier_id = random_int(1, supplier_count)
            cursor.execute(f"INSERT INTO {quoted('Orders')} (ProductID,SupplierID,OrderQty) VALUES (?,?,?)", (product_id,supplier_id,random_int(1,100)))

    conn.commit()
    messagebox.showinfo("Success", f"50 random records added for '{db_type}' (per relevant tables).")

# =========================
# View Table Data
# =========================
def view_table_data(table_name):
    if not table_name:
        messagebox.showerror("Error", "Select a table first")
        return
    for i in result_tree.get_children():
        result_tree.delete(i)
    tbl = sanitize_identifier(table_name)
    try:
        cursor.execute(f"PRAGMA table_info({quoted(tbl)})")
        cols = [c[1] for c in cursor.fetchall()]
        result_tree["columns"] = cols
        result_tree["show"] = "headings"
        for col in cols:
            result_tree.heading(col, text=col)
            result_tree.column(col, width=140, anchor="w")
        cursor.execute(f"SELECT * FROM {quoted(tbl)}")
        rows = cursor.fetchall()
        for row in rows:
            result_tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# =========================
# Execute Arbitrary Query
# =========================
def execute_user_query():
    sql = query_text.get("1.0", tk.END).strip()
    if not sql:
        messagebox.showerror("Error", "Enter an SQL statement")
        return
    for i in result_tree.get_children():
        result_tree.delete(i)
    try:
        cursor.execute(sql)
        if sql.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            cols = [desc[0] for desc in cursor.description]
            result_tree["columns"] = cols
            result_tree["show"] = "headings"
            for col in cols:
                result_tree.heading(col, text=col)
                result_tree.column(col, width=140, anchor="w")
            for row in rows:
                result_tree.insert("", tk.END, values=row)
            messagebox.showinfo("Query Result", f"{len(rows)} rows fetched.")
        else:
            conn.commit()
            messagebox.showinfo("Success", "Statement executed.")
            update_table_menu_values(db_type_var.get())
    except Exception as e:
        messagebox.showerror("SQL Error", str(e))

# =========================
# Help / Cheat Sheet
# =========================
def show_help():
    help_win = tk.Toplevel(root)
    help_win.title("SQL Help / Cheat Sheet")
    help_win.geometry("1000x650")
    text_area = scrolledtext.ScrolledText(help_win, width=120, height=40)
    text_area.pack(padx=5, pady=5)
    text_area.insert(tk.END, "=== SQL HELP / Cheat Sheet ===\nUse view table, add data, execute SQL queries.\n")
    text_area.config(state="disabled")

# =========================
# Exit
# =========================
def confirm_exit():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

# =========================
# UI Layout
# =========================
top_frame = ttk.Frame(root)
top_frame.pack(fill="x", padx=8, pady=6)

ttk.Label(top_frame, text="Select DB Template:").pack(side="left")
db_menu = ttk.Combobox(top_frame, textvariable=db_type_var, values=list(db_templates.keys()))
db_menu.pack(side="left", padx=5)
db_menu.bind("<<ComboboxSelected>>", lambda e: update_table_menu_values(db_type_var.get()))

ttk.Label(top_frame, text="Select Table:").pack(side="left", padx=5)
table_menu = ttk.Combobox(top_frame, textvariable=current_table)
table_menu.pack(side="left", padx=5)

btn_frame = ttk.Frame(root)
btn_frame.pack(fill="x", padx=8, pady=6)
ttk.Button(btn_frame, text="Add 50 Random Records (db-wide)", command=add_random_data).pack(side="left", padx=6)
ttk.Button(btn_frame, text="View Table", command=lambda: view_table_data(current_table.get())).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Help / Cheat Sheet", command=show_help).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Exit", command=confirm_exit).pack(side="left", padx=6)

query_frame = ttk.LabelFrame(root, text="Enter SQL Query")
query_frame.pack(fill="both", expand=True, padx=8, pady=6)
query_text = scrolledtext.ScrolledText(query_frame, height=7)
query_text.pack(fill="both", expand=True, padx=5, pady=5)
ttk.Button(query_frame, text="Execute SQL Query", command=execute_user_query).pack(pady=5)

result_frame = ttk.LabelFrame(root, text="Query Results / Table Data")
result_frame.pack(fill="both", expand=True, padx=8, pady=6)
result_tree = ttk.Treeview(result_frame)
result_tree.pack(fill="both", expand=True, padx=5, pady=5)

update_table_menu_values(db_type_var.get())
root.mainloop()