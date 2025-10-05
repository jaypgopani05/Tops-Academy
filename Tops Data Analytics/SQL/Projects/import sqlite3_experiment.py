#!/usr/bin/env python3
"""
SQL Playground - Rearranged Master File
Features: multi-DB templates, custom DB creator, PK/FK support, realistic random data,
SQL runner, result Treeview, export/import CSV, simple charts (matplotlib), status bar.
"""

# =========================
# Imports
# =========================
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import random
import string
import re
import csv
import sys

# matplotlib must set backend before importing pyplot when using TkAgg
try:
    import matplotlib
    matplotlib.use("TkAgg")
    import matplotlib.pyplot as plt
except Exception:
    matplotlib = None
    plt = None

# =========================
# Constants / Globals
# =========================
DB_FILENAME = "multi_db_playground.db"
WINDOW_TITLE = "SQL Playground - Multi-Database + Custom DB Creator"
WINDOW_GEOMETRY = "1400x820"
IDENT_RE = re.compile(r"[^A-Za-z0-9_]")

# =========================
# Root Tkinter Window
# =========================
root = tk.Tk()
root.title(WINDOW_TITLE)
root.geometry(WINDOW_GEOMETRY)

# =========================
# Database Connection and PRAGMA
# =========================
conn = sqlite3.connect(DB_FILENAME)
cursor = conn.cursor()
# Enforce foreign keys
try:
    cursor.execute("PRAGMA foreign_keys = ON")
    conn.commit()
except Exception:
    # not fatal, but warn
    print("Warning: Could not enable PRAGMA foreign_keys", file=sys.stderr)

# =========================
# Helper functions (random data + sanitization)
# =========================
def sanitize_identifier(name: str) -> str:
    """Return a safe identifier: remove/replace illegal chars, avoid starting with digit."""
    if not name:
        raise ValueError("Empty identifier")
    s = IDENT_RE.sub("_", name.strip())
    if s and s[0].isdigit():
        s = "_" + s
    return s

def quoted(name: str) -> str:
    """Return a properly quoted identifier for SQL. We sanitize then quote to be safe."""
    s = sanitize_identifier(name)
    return f'"{s}"'

def random_string(length=6) -> str:
    """Alphabetic random string."""
    return "".join(random.choices(string.ascii_letters, k=length))

def random_text(prefix="Txt", length=6) -> str:
    """Backward-compatible short random text (kept for compatibility)."""
    return f"{''.join(random.choices(string.ascii_lowercase, k=length))}"

def random_int(low=1, high=100) -> int:
    return random.randint(low, high)

def random_real(low=1.0, high=1000.0) -> float:
    return round(random.uniform(low, high), 2)

def random_phone() -> str:
    """Return an Indian-style phone number string."""
    return f"+91-{random.randint(6000000000, 9999999999)}"

def random_email_local(first="user", last="id") -> str:
    """Basic email local part generator."""
    local = f"{first.lower()}.{last.lower()}"
    local = re.sub(r"[^a-z0-9.]", "", local)
    domains = ["example.com", "gmail.com", "yahoo.com", "outlook.com", "mail.com"]
    return f"{local}@{random.choice(domains)}"

# realistic data sets
FIRST_NAMES = [
    "Aarav","Vivaan","Aditya","Vihaan","Arjun","Sai","Rohan","Krishna","Ishaan","Kabir",
    "Saanvi","Ananya","Diya","Aadhya","Ira","Myra","Aanya","Sofia","Meera","Anika"
]
LAST_NAMES = [
    "Sharma","Verma","Patel","Singh","Kumar","Gupta","Reddy","Nair","Mehta","Joshi",
    "Kapoor","Agarwal","Khan","Chopra","Bose","Das","Ghosh","Iyer","Nanda","Prasad"
]
CITIES = [
    "Mumbai","Delhi","Bengaluru","Kolkata","Chennai","Hyderabad","Pune","Ahmedabad","Surat","Jaipur",
    "Lucknow","Kanpur","Nagpur","Indore","Thane"
]
COMPANY_WORDS = ["Solutions","Technologies","Systems","Global","Enterprises","Labs","Works","Dynamics","Innovations"]
PRODUCT_ADJS = ["Smart","Ultra","Pro","Neo","Max","Eco","Prime","Plus","One","Mini"]
PRODUCT_NOUNS = ["Sensor","Hub","Charge","Drive","Monitor","Link","Pad","Mate","Box","Core"]

def realistic_first_name():
    return random.choice(FIRST_NAMES)

def realistic_last_name():
    return random.choice(LAST_NAMES)

def realistic_phone():
    first = str(random.choice([6,7,8,9]))
    rest = "".join(random.choices(string.digits, k=9))
    return f"+91-{first}{rest}"

def realistic_email(first=None, last=None):
    if not first or not last:
        first = random_string(5)
        last = random_string(3)
    return random_email_local(first, last)

def realistic_city():
    return random.choice(CITIES)

def realistic_company_name():
    return f"{random.choice(['Apex','Nova','Axis','Quantum','Prime','Blue'])} {random.choice(COMPANY_WORDS)}"

def realistic_product_name():
    return f"{random.choice(PRODUCT_ADJS)} {random.choice(PRODUCT_NOUNS)} {random.randint(100,999)}"

def realistic_address():
    num = random.randint(1,999)
    street = random.choice(["MG Road","Station Road","North Street","Park Avenue","Main Street","Industrial Area"])
    city = realistic_city()
    return f"{num} {street}, {city}"

# =========================
# Database templates (predefined)
# Each template is a dict of table -> list of (column_name, column_type_fragment)
# The create_tables function interprets and creates appropriate SQL.
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




#ADD HERE





# =========================
# Core DB Functions
# - create_tables: creates schema for given db_type (uses heuristics for PK)
# - update_table_menu_values: updates combobox of tables
# =========================

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Departments (
#     DeptID INTEGER PRIMARY KEY AUTOINCREMENT,
#     DeptName TEXT
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Employees (
#     EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
#     FirstName TEXT,
#     LastName TEXT,
#     DeptID INTEGER,
#     FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
# )
# """)





#Complete function here





def create_tables(db_type):
    """Create tables for a db_type using db_templates; add PK autoincrement where column endswith ID."""
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
            # If column looks like an ID (endswith ID) and type is INTEGER, treat as primary autoinc
            if c.upper().endswith("ID") and ("INT" in t):
                col_def = f'{quoted(c)} INTEGER PRIMARY KEY AUTOINCREMENT'
            else:
                col_def = f'{quoted(c)} {t}'
            col_defs_list.append(col_def)
        col_defs = ", ".join(col_defs_list)
        sql = f'CREATE TABLE IF NOT EXISTS {quoted(tbl)} ({col_defs})'
        try:
            cursor.execute(sql)
        except Exception as e:
            messagebox.showerror("SQL Error", f"Failed creating table {raw_table_name}:\n{e}")
            return
    conn.commit()
    update_table_menu_values(db_type)

def update_table_menu_values(selected_db=None):
    """Refresh table combobox values from db_templates for selected_db."""
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
# Add realistic random data (50 rows per run)
# - Preserves relational logic for built-in templates
# - For custom templates, inserts based on PRAGMA table_info
# =========================
def add_random_data():
    db_type = db_type_var.get()
    if db_type not in db_templates:
        messagebox.showerror("Error", "Select or create a valid database type first.")
        return
    # Ensure tables are created
    create_tables(db_type)
    tables = db_templates[db_type]["tables"]

    if db_type == "Organization":
        # Ensure departments exist
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Departments'))}")
            deps = cursor.fetchone()[0]
        except Exception:
            deps = 0
        if deps == 0:
            depts = ["HR","Finance","IT","Marketing","Sales","Admin","Legal","Operations","R&D","Support"]
            for d in depts:
                cursor.execute(
                    f"INSERT INTO {quoted(sanitize_identifier('Departments'))} ({quoted('DeptName')},{quoted('Location')}) VALUES (?,?)",
                    (d, realistic_city())
                )
            conn.commit()

        for _ in range(50):
            # realistic employee
            dept_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Departments'))}").fetchone()[0] or 1
            first = realistic_first_name()
            last = realistic_last_name()
            dept_id = random_int(1, max(1, dept_count))
            cursor.execute(
                f"INSERT INTO {quoted(sanitize_identifier('Employees'))} ({quoted('FirstName')},{quoted('LastName')},{quoted('DeptID')}) VALUES (?,?,?)",
                (first, last, dept_id)
            )
            emp_id = cursor.lastrowid
            cursor.execute(
                f"INSERT INTO {quoted(sanitize_identifier('Salaries'))} ({quoted('EmpID')},{quoted('SalaryAmount')}) VALUES (?,?)",
                (emp_id, random_int(40000,150000))
            )
            # create project and assign
            project_name = realistic_product_name()
            cursor.execute(
                f"INSERT INTO {quoted(sanitize_identifier('Projects'))} ({quoted('ProjectName')}) VALUES (?)",
                (project_name,)
            )
            project_id = cursor.lastrowid
            try:
                cursor.execute(
                    f"INSERT OR IGNORE INTO {quoted(sanitize_identifier('EmployeeProjects'))} ({quoted('EmpID')},{quoted('ProjectID')}) VALUES (?,?)",
                    (emp_id, project_id)
                )
            except Exception:
                pass

    elif db_type == "Students":
        # ensure courses exist
        try:
            course_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Courses'))}").fetchone()[0]
        except Exception:
            course_count = 0
        if course_count == 0:
            sample = ["Math","Physics","Chemistry","History","English"]
            for s in sample:
                cursor.execute(
                    f"INSERT INTO {quoted(sanitize_identifier('Courses'))} ({quoted('CourseName')},{quoted('Credits')}) VALUES (?,?)",
                    (s, random_int(2,5))
                )
            conn.commit()
        for _ in range(50):
            first = realistic_first_name()
            last = realistic_last_name()
            age = random_int(15,30)
            cursor.execute(
                f"INSERT INTO {quoted(sanitize_identifier('Students'))} ({quoted('FirstName')},{quoted('LastName')},{quoted('Age')}) VALUES (?,?,?)",
                (first, last, age)
            )
            student_id = cursor.lastrowid
            course_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Courses'))}").fetchone()[0] or 1
            course_id = random_int(1, course_count)
            cursor.execute(
                f"INSERT INTO {quoted(sanitize_identifier('Enrollments'))} ({quoted('StudentID')},{quoted('CourseID')},{quoted('Grade')}) VALUES (?,?,?)",
                (student_id, course_id, random.choice(["A","B","C","D"]))
            )

    elif db_type == "Inventory":
        try:
            sup_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Suppliers'))}").fetchone()[0]
        except Exception:
            sup_count = 0
        if sup_count == 0:
            for i in range(5):
                cursor.execute(
                    f"INSERT INTO {quoted(sanitize_identifier('Suppliers'))} ({quoted('SupplierName')},{quoted('Contact')}) VALUES (?,?)",
                    (realistic_company_name(), realistic_phone())
                )
            conn.commit()
        for _ in range(50):
            product = realistic_product_name()
            price = random_real(10,500)
            cursor.execute(
                f"INSERT INTO {quoted(sanitize_identifier('Products'))} ({quoted('ProductName')},{quoted('Price')}) VALUES (?,?)",
                (product, price)
            )
            product_id = cursor.lastrowid
            supplier_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Suppliers'))}").fetchone()[0] or 1
            supplier_id = random_int(1, supplier_count)
            cursor.execute(
                f"INSERT INTO {quoted(sanitize_identifier('Orders'))} ({quoted('ProductID')},{quoted('SupplierID')},{quoted('OrderQty')}) VALUES (?,?,?)",
                (product_id, supplier_id, random_int(1,100))
            )

    else:
        # generic/custom templates
        create_tables(db_type)
        for table_name, cols in db_templates[db_type]["tables"].items():
            tbl = sanitize_identifier(table_name)
            try:
                cursor.execute(f"PRAGMA table_info({quoted(tbl)})")
                pragma = cursor.fetchall()  # (cid, name, type, notnull, dflt_value, pk)
                insert_cols = [col_info[1] for col_info in pragma if col_info[5] == 0]
            except Exception:
                insert_cols = [sanitize_identifier(c[0]) for c in cols]

            if not insert_cols:
                continue
            placeholders = ", ".join(["?"] * len(insert_cols))
            col_list_sql = ", ".join([quoted(c) for c in insert_cols])
            col_type_map = {sanitize_identifier(cn).lower(): ctype.upper() for cn, ctype in cols}

            for _ in range(50):
                values = []
                for col in insert_cols:
                    typ = col_type_map.get(col.lower(), "TEXT")
                    low = col.lower()
                    if "INT" in typ.upper():
                        values.append(random_int(1, 1000))
                    elif "REAL" in typ.upper() or "FLOA" in typ.upper() or "DOUB" in typ.upper():
                        values.append(random_real(1, 10000))
                    else:
                        # heuristics
                        if "email" in low:
                            values.append(realistic_email(realistic_first_name(), realistic_last_name()))
                        elif "phone" in low or "contact" in low:
                            values.append(realistic_phone())
                        elif "name" in low:
                            if "supplier" in low or "company" in low:
                                values.append(realistic_company_name())
                            else:
                                values.append(f"{realistic_first_name()} {realistic_last_name()}")
                        elif "addr" in low or "city" in low or "location" in low:
                            values.append(realistic_address())
                        elif "price" in low or "amount" in low or "qty" in low:
                            values.append(random_int(1,1000))
                        else:
                            values.append(random_text(col[:3],6))
                sql = f"INSERT INTO {quoted(tbl)} ({col_list_sql}) VALUES ({placeholders})"
                try:
                    cursor.execute(sql, values)
                except Exception as e:
                    print(f"Insert error for {tbl}: {e}", file=sys.stderr)
                    continue

    conn.commit()
    messagebox.showinfo("Success", f"50 random records added for '{db_type}' (per relevant tables).")

# =========================
# View Table Data
# =========================
def view_table_data(table_name):
    if not table_name:
        messagebox.showerror("Error", "Select a table first")
        return
    # Clear treeview
    for i in result_tree.get_children():
        result_tree.delete(i)
    tbl = sanitize_identifier(table_name)
    try:
        cursor.execute(f"PRAGMA table_info({quoted(tbl)})")
        cols = [c[1] for c in cursor.fetchall()]
        # Configure treeview columns
        result_tree["columns"] = cols
        result_tree["show"] = "headings"
        for col in cols:
            result_tree.heading(col, text=col)
            result_tree.column(col, width=140, anchor="w")
        cursor.execute(f"SELECT * FROM {quoted(tbl)}")
        rows = cursor.fetchall()
        for row in rows:
            result_tree.insert("", tk.END, values=row)
        set_status(f"Displayed {len(rows)} rows from {table_name}")
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
    # Clear old results
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
            set_status(f"Query executed: {len(rows)} rows shown.")
        else:
            conn.commit()
            messagebox.showinfo("Success", "Statement executed.")
            update_table_menu_values(db_type_var.get())
            set_status("Non-select statement executed and committed.")
    except Exception as e:
        messagebox.showerror("SQL Error", str(e))
        set_status("Last query failed.")

# =========================
# Dynamic Help / Cheat Sheet
# =========================
def show_help():
    help_win = tk.Toplevel(root)
    help_win.title("SQL Help / Cheat Sheet")
    help_win.geometry("1000x650")
    text_area = scrolledtext.ScrolledText(help_win, width=120, height=40)
    text_area.pack(padx=5, pady=5)

    db_type = db_type_var.get()
    if db_type not in db_templates:
        text_area.insert(tk.END, f"No template info for '{db_type}'. You can still run queries against created tables.\n")
        text_area.config(state="disabled")
        return

    tables = db_templates[db_type]["tables"]
    help_text = f"===== SQL HELP / EXAMPLES for {db_type} =====\n\n"

    # DDL
    help_text += "-- DDL Examples --\n"
    for t in tables:
        help_text += f"CREATE TABLE {t} (...);\n"
    help_text += "ALTER TABLE table_name ADD COLUMN col_name TYPE;\nDROP TABLE table_name;\n\n"

    # SELECTs
    help_text += "-- SELECT Examples --\n"
    for t in tables:
        help_text += f"SELECT * FROM {t};\n"
        help_text += f"SELECT COUNT(*) FROM {t};\n"
        help_text += f"SELECT * FROM {t} ORDER BY ROWID DESC LIMIT 10;\n"
    help_text += "\n"

    # JOIN examples tailored
    help_text += "-- JOIN Examples --\n"
    if db_type == "Organization":
        help_text += (
            "SELECT e.FirstName, s.SalaryAmount FROM Employees e INNER JOIN Salaries s ON e.EmpID=s.EmpID;\n"
            "SELECT e.FirstName, p.ProjectName FROM Employees e\n  INNER JOIN EmployeeProjects ep ON e.EmpID=ep.EmpID\n  INNER JOIN Projects p ON ep.ProjectID=p.ProjectID;\n\n"
        )
    elif db_type == "Students":
        help_text += (
            "SELECT s.FirstName, c.CourseName, e.Grade FROM Students s\n  INNER JOIN Enrollments e ON s.StudentID=e.StudentID\n  INNER JOIN Courses c ON e.CourseID=c.CourseID;\n\n"
        )
    elif db_type == "Inventory":
        help_text += (
            "SELECT p.ProductName, o.OrderQty, s.SupplierName FROM Products p\n  INNER JOIN Orders o ON p.ProductID=o.ProductID\n  INNER JOIN Suppliers s ON o.SupplierID=s.SupplierID;\n\n"
        )
    else:
        help_text += "-- Generic join example --\nSELECT t1.col, t2.col FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.table1_id;\n\n"

    # Insert / Update / Delete examples (use actual columns)
    help_text += "-- INSERT / UPDATE / DELETE Examples --\n"
    for t, cols in tables.items():
        non_pk_cols = [c for c in cols if not (c[0].upper().endswith("ID") and "INT" in c[1].upper())]
        col_names = ", ".join([c[0] for c in non_pk_cols]) if non_pk_cols else ", ".join([c[0] for c in cols])
        sample_vals = ", ".join([("'example'" if "TEXT" in c[1].upper() else "100") for c in non_pk_cols]) if non_pk_cols else ""
        if sample_vals:
            help_text += f"INSERT INTO {t} ({col_names}) VALUES ({sample_vals});\n"
        update_col = non_pk_cols[0][0] if non_pk_cols else cols[0][0]
        update_sample = "\"new\"" if "TEXT" in (non_pk_cols[0][1] if non_pk_cols else cols[0][1]).upper() else "123"
        help_text += f"UPDATE {t} SET {update_col} = {update_sample} WHERE ROWID = 1;\n"
        help_text += f"DELETE FROM {t} WHERE ROWID = 1;\n\n"

    # Aggregates & Subqueries
    help_text += "-- AGGREGATES & Subqueries --\n"
    for t in tables:
        first_col = tables[t][0][0] if tables[t] else "*"
        help_text += f"SELECT COUNT(*), AVG({first_col if first_col else '*'}) FROM {t};\n"
    help_text += "\n-- Subquery Example --\n"
    tlist = list(tables.keys())
    if len(tlist) >= 2:
        help_text += f"SELECT * FROM {tlist[0]} WHERE ROWID IN (SELECT ROWID FROM {tlist[1]} LIMIT 5);\n"
    help_text += "\n"

    # CTE / Window function examples
    help_text += "-- CTE / Window function examples --\n"
    help_text += "WITH tmp AS (SELECT * FROM table_name LIMIT 10) SELECT * FROM tmp;\n"
    help_text += "SELECT col, ROW_NUMBER() OVER (ORDER BY col) FROM table_name;\n"

    text_area.insert(tk.END, help_text)
    text_area.config(state="disabled")

# =========================
# Custom Database Creator (GUI)
# =========================
def open_custom_db_creator():
    win = tk.Toplevel(root)
    win.title("Custom Database Creator")
    win.geometry("700x500")

    ttk.Label(win, text="Custom DB Name:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
    db_name_var = tk.StringVar()
    ttk.Entry(win, textvariable=db_name_var).grid(row=0, column=1, padx=8, pady=8, sticky="we")

    table_defs = []  # list of (table_name, [(col_name, col_type), ...])

    def add_table():
        tbl_win = tk.Toplevel(win)
        tbl_win.title("Add Table")
        tbl_win.geometry("480x320")

        ttk.Label(tbl_win, text="Table name:").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        tbl_name_var = tk.StringVar()
        ttk.Entry(tbl_win, textvariable=tbl_name_var).grid(row=0, column=1, padx=6, pady=6, sticky="we")

        cols_frame = ttk.Frame(tbl_win)
        cols_frame.grid(row=1, column=0, columnspan=2, padx=6, pady=6, sticky="nsew")
        cols_frame.columnconfigure(1, weight=1)

        col_rows = []

        def add_column_row():
            r = len(col_rows)
            col_name = tk.StringVar()
            col_type = tk.StringVar(value="TEXT")
            ttk.Entry(cols_frame, textvariable=col_name).grid(row=r, column=0, padx=4, pady=4, sticky="we")
            ttk.Combobox(cols_frame, textvariable=col_type, values=["TEXT", "INTEGER", "REAL", "DATE", "DATETIME"]).grid(
                row=r, column=1, padx=4, pady=4, sticky="we"
            )
            col_rows.append((col_name, col_type))

        def save_table():
            name = tbl_name_var.get().strip()
            if not name or not col_rows:
                messagebox.showerror("Error", "Provide table name and at least one column")
                return
            cols = []
            for cn, ct in col_rows:
                cname = cn.get().strip()
                ctype = ct.get().strip().upper()
                if not cname:
                    messagebox.showerror("Error", "Column name cannot be empty")
                    return
                cols.append((cname, ctype))
            table_defs.append((name, cols))
            messagebox.showinfo("Table added", f"Table '{name}' with {len(cols)} columns added to custom DB.")
            tbl_win.destroy()

        ttk.Button(tbl_win, text="Add Column", command=add_column_row).grid(row=2, column=0, padx=6, pady=6, sticky="w")
        ttk.Button(tbl_win, text="Save Table", command=save_table).grid(row=2, column=1, padx=6, pady=6, sticky="e")

    def save_database():
        db_name = db_name_var.get().strip()
        if not db_name:
            messagebox.showerror("Error", "Please enter database name")
            return
        if not table_defs:
            messagebox.showerror("Error", "Add at least one table")
            return
        user_key = db_name
        if user_key in db_templates:
            if not messagebox.askyesno("Overwrite?", f"Template '{user_key}' already exists. Overwrite?"):
                return
        db_templates[user_key] = {"tables": {}}
        for tbl_name, cols in table_defs:
            db_templates[user_key]["tables"][tbl_name] = [(cname, ctype) for cname, ctype in cols]
        # create tables physically
        create_tables(user_key)
        # set as active DB and update UI
        db_menu["values"] = list(db_templates.keys())
        db_menu.set(user_key)
        db_type_var.set(user_key)
        update_table_menu_values(user_key)
        win.destroy()
        messagebox.showinfo("Custom DB", f"Custom DB '{user_key}' created, initialized and set active.")

    ttk.Button(win, text="Add Table", command=add_table).grid(row=3, column=0, padx=8, pady=10, sticky="w")
    ttk.Button(win, text="Save Custom DB", command=save_database).grid(row=3, column=1, padx=8, pady=10, sticky="e")

# =========================
# UI Layout - Top Controls
# =========================
top_frame = ttk.Frame(root)
top_frame.pack(fill="x", padx=8, pady=8)

ttk.Label(top_frame, text="Select Database Type:").pack(side="left", padx=6)
db_menu = ttk.Combobox(top_frame, textvariable=db_type_var, values=list(db_templates.keys()), state="readonly", width=30)
db_menu.pack(side="left", padx=6)
ttk.Button(top_frame, text="Initialize / Create Tables", command=lambda: create_tables(db_type_var.get())).pack(side="left", padx=6)
ttk.Button(top_frame, text="Create Custom DB...", command=open_custom_db_creator).pack(side="left", padx=6)

ttk.Label(top_frame, text="Select Table:").pack(side="left", padx=12)
table_menu = ttk.Combobox(top_frame, textvariable=current_table, values=[], state="readonly", width=30)
table_menu.pack(side="left", padx=6)

# =========================
# Buttons Frame
# =========================
btn_frame = ttk.Frame(root)
btn_frame.pack(fill="x", padx=8, pady=6)

ttk.Button(btn_frame, text="Add 50 Random Records (db-wide)", command=add_random_data).pack(side="left", padx=6)
ttk.Button(btn_frame, text="View Table", command=lambda: view_table_data(current_table.get())).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Help / Cheat Sheet", command=show_help).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Create Custom DB...", command=open_custom_db_creator).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Exit", command=root.destroy).pack(side="left", padx=5)

# =========================
# Query Frame (SQL Runner)
# =========================
query_frame = tk.LabelFrame(root, text="Execute SQL Query")
query_frame.pack(fill=tk.X, padx=5, pady=5)
query_text = scrolledtext.ScrolledText(query_frame, height=6)
query_text.pack(fill=tk.X, padx=5, pady=5)
ttk.Button(query_frame, text="Run SQL", command=execute_user_query).pack(side=tk.RIGHT, padx=5, pady=5)

# =========================
# Results Area (Treeview)
# =========================
result_frame = ttk.Frame(root)
result_frame.pack(fill="both", expand=True, padx=8, pady=8)
result_tree = ttk.Treeview(result_frame)
result_tree.pack(fill="both", expand=True, side="left")
vsb = ttk.Scrollbar(result_frame, orient="vertical", command=result_tree.yview)
vsb.pack(side="right", fill="y")
result_tree.configure(yscrollcommand=vsb.set)

# =========================
# Status Bar (bottom)
# =========================
status_var = tk.StringVar(value="Ready.")
status_bar = ttk.Label(root, textvariable=status_var, relief="sunken", anchor="w")
status_bar.pack(fill="x", side="bottom")

def set_status(msg: str):
    status_var.set(msg)
    root.update_idletasks()

# =========================
# Export Query Results to CSV
# =========================
def export_results_to_csv():
    rows = []
    cols = result_tree["columns"]
    for item in result_tree.get_children():
        rows.append(result_tree.item(item)["values"])
    if not rows or not cols:
        messagebox.showerror("Export Error", "No data to export.")
        return
    fname = simpledialog.askstring("Export CSV", "Enter filename (without extension):")
    if not fname:
        return
    fname = fname.strip() + ".csv"
    try:
        with open(fname, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(cols)
            writer.writerows(rows)
        messagebox.showinfo("Exported", f"Results exported to {fname}")
        set_status(f"Exported to {fname}")
    except Exception as e:
        messagebox.showerror("Export Error", str(e))
        set_status("Export failed.")

ttk.Button(btn_frame, text="Export Results to CSV", command=export_results_to_csv).pack(side="left", padx=6)

# =========================
# Import CSV into Table
# =========================
def import_csv_to_table():
    import tkinter.filedialog as fd
    tbl = current_table.get()
    if not tbl:
        messagebox.showerror("Import Error", "Select a table first.")
        return
    file_path = fd.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            cursor.execute(f"PRAGMA table_info({quoted(sanitize_identifier(tbl))})")
            table_cols = [c[1] for c in cursor.fetchall()]
            import_cols = [h for h in headers if h in table_cols]
            if not import_cols:
                messagebox.showerror("Import Error", "CSV columns do not match table columns.")
                return
            col_sql = ", ".join([quoted(c) for c in import_cols])
            placeholders = ", ".join(["?"] * len(import_cols))
            count = 0
            for row in reader:
                values = [row[headers.index(c)] for c in import_cols]
                cursor.execute(f"INSERT INTO {quoted(sanitize_identifier(tbl))} ({col_sql}) VALUES ({placeholders})", values)
                count += 1
            conn.commit()
        messagebox.showinfo("Import Complete", f"Imported {count} rows into {tbl}.")
        set_status(f"Imported {count} rows into {tbl}.")
    except Exception as e:
        messagebox.showerror("Import Error", str(e))
        set_status("Import failed.")

ttk.Button(btn_frame, text="Import CSV to Table", command=import_csv_to_table).pack(side="left", padx=6)

# =========================
# Simple Analytics / Chart (matplotlib)
# =========================
def show_chart():
    if matplotlib is None or plt is None:
        messagebox.showerror("Chart Error", "matplotlib not available.")
        return
    tbl = current_table.get()
    if not tbl:
        messagebox.showerror("Chart Error", "Select a table first.")
        return
    cursor.execute(f"PRAGMA table_info({quoted(sanitize_identifier(tbl))})")
    cols = [c[1] for c in cursor.fetchall()]
    col = simpledialog.askstring("Chart", f"Enter column name to chart (from: {', '.join(cols)}):")
    if not col or col not in cols:
        messagebox.showerror("Chart Error", "Invalid column name.")
        return
    try:
        cursor.execute(f"SELECT {quoted(col)}, COUNT(*) FROM {quoted(sanitize_identifier(tbl))} GROUP BY {quoted(col)} ORDER BY COUNT(*) DESC LIMIT 10")
        data = cursor.fetchall()
        if not data:
            messagebox.showerror("Chart Error", "No data to chart.")
            return
        labels, counts = zip(*data)
        plt.figure(figsize=(8,5))
        plt.bar(labels, counts)
        plt.title(f"Top 10 {col} values in {tbl}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        set_status(f"Chart displayed for {col} in {tbl}.")
    except Exception as e:
        messagebox.showerror("Chart Error", str(e))
        set_status("Chart failed.")

ttk.Button(btn_frame, text="Show Chart", command=show_chart).pack(side="left", padx=6)

# =========================
# Bindings & Initialization
# =========================
def on_db_change(*args):
    update_table_menu_values(db_type_var.get())

db_type_var.trace_add("write", on_db_change)

# initialize table menu & default DB on startup
update_table_menu_values(db_type_var.get())

set_status("Ready. SQL Playground loaded.")

# =========================
# Mainloop
# =========================
root.mainloop()
