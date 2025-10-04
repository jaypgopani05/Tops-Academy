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
    """Return a safe identifier: remove/replace illegal chars, avoid starting with digit."""
    if not name:
        raise ValueError("Empty identifier")
    # replace illegal chars with underscore
    s = IDENT_RE.sub("_", name.strip())
    # if starts with digit, prefix with _
    if s[0].isdigit():
        s = "_" + s
    return s

def quoted(name: str) -> str:
    """Return a properly quoted identifier for SQL. We sanitize then quote to be safe."""
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
# Current DB Type & UI vars
# =========================
db_type_var = tk.StringVar(value="Organization")
current_table = tk.StringVar()

# =========================
# Helpers: simple fake generators
# =========================
def random_text(prefix="Txt", length=6):
    return f"{prefix}_{''.join(random.choices(string.ascii_lowercase, k=length))}"

def random_int(low=1, high=100):
    return random.randint(low, high)

def random_real(low=1.0, high=1000.0):
    return round(random.uniform(low, high), 2)

def random_text(prefix="Txt", length=6):
    return f"{prefix}_{''.join(random.choices(string.ascii_lowercase, k=length))}"

# =========================
# Create tables for a db_type (predefined or custom)
# Safe: sanitize and quote identifiers
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
            # If column looks like an ID (endswith ID) and type is INTEGER, make it primary autoinc
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
    # Informational but not annoying: only show when user explicitly inits (button)
    # messagebox.showinfo("Tables initialized", f"Tables for '{db_type}' are ready.")

# =========================
# Update table-menu options
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
# Add random data for selected db (50 records per run)
# - For built-in templates we preserve relational logic
# - For custom templates we insert based on column type (TEXT/INTEGER/REAL)
# =========================
def add_random_data():
    db_type = db_type_var.get()
    if db_type not in db_templates:
        messagebox.showerror("Error", "Select or create a valid database type first.")
        return
    tables = db_templates[db_type]["tables"]

    # Ensure tables are created
    create_tables(db_type)

    # ORGANIZATION logic
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
                cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Departments'))} ({quoted('DeptName')},{quoted('Location')}) VALUES (?,?)", (d, random_text("City",4)))
            conn.commit()

        for _ in range(50):
            # Insert employee
            dept_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Departments'))}").fetchone()[0] or 1
            first = random_text("F",5).capitalize()
            last = random_text("L",6).capitalize()
            dept_id = random_int(1, max(1, dept_count))
            cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Employees'))} ({quoted('FirstName')},{quoted('LastName')},{quoted('DeptID')}) VALUES (?,?,?)", (first, last, dept_id))
            emp_id = cursor.lastrowid
            cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Salaries'))} ({quoted('EmpID')},{quoted('SalaryAmount')}) VALUES (?,?)", (emp_id, random_int(40000,150000)))
            cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Projects'))} ({quoted('ProjectName')}) VALUES (?)", (random_text("Project",5),))
            project_id = cursor.lastrowid
            try:
                cursor.execute(f"INSERT OR IGNORE INTO {quoted(sanitize_identifier('EmployeeProjects'))} ({quoted('EmpID')},{quoted('ProjectID')}) VALUES (?,?)", (emp_id, project_id))
            except Exception:
                pass

    # STUDENTS logic
    elif db_type == "Students":
        # Ensure at least one course
        try:
            course_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Courses'))}").fetchone()[0]
        except Exception:
            course_count = 0
        if course_count == 0:
            sample = ["Math","Physics","Chemistry","History","English"]
            for s in sample:
                cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Courses'))} ({quoted('CourseName')},{quoted('Credits')}) VALUES (?,?)", (s, random_int(2,5)))
            conn.commit()
        for _ in range(50):
            first = random_text("S",5).capitalize()
            last = random_text("S",6).capitalize()
            age = random_int(15,30)
            cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Students'))} ({quoted('FirstName')},{quoted('LastName')},{quoted('Age')}) VALUES (?,?,?)", (first, last, age))
            student_id = cursor.lastrowid
            course_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Courses'))}").fetchone()[0] or 1
            course_id = random_int(1, course_count)
            cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Enrollments'))} ({quoted('StudentID')},{quoted('CourseID')},{quoted('Grade')}) VALUES (?,?,?)", (student_id, course_id, random.choice(["A","B","C","D"])))

    # INVENTORY logic
    elif db_type == "Inventory":
        try:
            sup_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Suppliers'))}").fetchone()[0]
        except Exception:
            sup_count = 0
        if sup_count == 0:
            for i in range(5):
                cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Suppliers'))} ({quoted('SupplierName')},{quoted('Contact')}) VALUES (?,?)", (random_text("Supplier",4), random_text("Phone",6)))
            conn.commit()
        for _ in range(50):
            product = random_text("Prod",5)
            price = random_real(10,500)
            cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Products'))} ({quoted('ProductName')},{quoted('Price')}) VALUES (?,?)", (product, price))
            product_id = cursor.lastrowid
            supplier_count = cursor.execute(f"SELECT COUNT(*) FROM {quoted(sanitize_identifier('Suppliers'))}").fetchone()[0] or 1
            supplier_id = random_int(1, supplier_count)
            cursor.execute(f"INSERT INTO {quoted(sanitize_identifier('Orders'))} ({quoted('ProductID')},{quoted('SupplierID')},{quoted('OrderQty')}) VALUES (?,?,?)", (product_id, supplier_id, random_int(1,100)))

    # CUSTOM / OTHER templates
    else:
        create_tables(db_type)
        for table_name, cols in db_templates[db_type]["tables"].items():
            tbl = sanitize_identifier(table_name)
            # find insertable columns via PRAGMA (skip primary key columns)
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

            # build type map from template (best-effort)
            col_type_map = {sanitize_identifier(cn).lower(): ctype.upper() for cn, ctype in cols}

            for _ in range(50):
                values = []
                for col in insert_cols:
                    typ = col_type_map.get(col.lower(), "TEXT")
                    if "INT" in typ:
                        values.append(random_int(1, 1000))
                    elif "REAL" in typ or "FLOA" in typ or "DOUB" in typ:
                        values.append(random_real(1, 10000))
                    else:
                        low = col.lower()
                        if "email" in low:
                            values.append(f"{random_text('user',5).lower()}@example.com")
                        elif "phone" in low or "contact" in low:
                            values.append(f"+91-{random_int(6000000000,9999999999)}")
                        elif "name" in low:
                            values.append(random_text("Name",6).capitalize())
                        else:
                            values.append(random_text(col[:3],6))
                sql = f"INSERT INTO {quoted(tbl)} ({col_list_sql}) VALUES ({placeholders})"
                try:
                    cursor.execute(sql, values)
                except Exception as e:
                    # skip problematic inserts but continue
                    print(f"Insert error for {tbl}: {e}")
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
    # Clear tree
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
        help_text += "SELECT e.FirstName, s.SalaryAmount FROM Employees e INNER JOIN Salaries s ON e.EmpID=s.EmpID;\n"
        help_text += "SELECT e.FirstName, p.ProjectName FROM Employees e\n  INNER JOIN EmployeeProjects ep ON e.EmpID=ep.EmpID\n  INNER JOIN Projects p ON ep.ProjectID=p.ProjectID;\n\n"
    elif db_type == "Students":
        help_text += "SELECT s.FirstName, c.CourseName, e.Grade FROM Students s\n  INNER JOIN Enrollments e ON s.StudentID=e.StudentID\n  INNER JOIN Courses c ON e.CourseID=c.CourseID;\n\n"
    elif db_type == "Inventory":
        help_text += "SELECT p.ProductName, o.OrderQty, s.SupplierName FROM Products p\n  INNER JOIN Orders o ON p.ProductID=o.ProductID\n  INNER JOIN Suppliers s ON o.SupplierID=s.SupplierID;\n\n"
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
        # safe fallback for UPDATE: attempt to use a non-PK column or the first column
        update_col = non_pk_cols[0][0] if non_pk_cols else cols[0][0]
        update_sample = "\"new\"" if "TEXT" in (non_pk_cols[0][1] if non_pk_cols else cols[0][1]).upper() else "123"
        help_text += f"UPDATE {t} SET {update_col} = {update_sample} WHERE ROWID = 1;\n"
        help_text += f"DELETE FROM {t} WHERE ROWID = 1;\n\n"

    # Aggregates & Subqueries
    help_text += "-- Aggregates & Subqueries --\n"
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
# Custom Database Creator
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
            ttk.Combobox(cols_frame, textvariable=col_type, values=["TEXT", "INTEGER", "REAL", "DATE"]).grid(row=r, column=1, padx=4, pady=4, sticky="we")
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
        # register new template
        # sanitize DB template key to a friendly label (we keep user's raw name as key)
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
# UI Layout
# =========================
# Top frame: database selection and init plus custom db creator
top_frame = ttk.Frame(root)
top_frame.pack(fill="x", padx=8, pady=8)

ttk.Label(top_frame, text="Select Database Type:").pack(side="left", padx=6)
db_menu = ttk.Combobox(top_frame, textvariable=db_type_var, values=list(db_templates.keys()), state="readonly", width=30)
db_menu.pack(side="left", padx=6)
ttk.Button(top_frame, text="Initialize / Create Tables", command=lambda: create_tables(db_type_var.get())).pack(side="left", padx=6)
ttk.Button(top_frame, text="Create Custom DB...", command=open_custom_db_creator).pack(side="left", padx=6)


# Table selection
ttk.Label(top_frame, text="Select Table:").pack(side="left", padx=12)
table_menu = ttk.Combobox(top_frame, textvariable=current_table, values=[], state="readonly", width=30)
table_menu.pack(side="left", padx=6)

# Buttons frame
btn_frame = ttk.Frame(root)
btn_frame.pack(fill="x", padx=8, pady=6)

ttk.Button(btn_frame, text="Add 50 Random Records (db-wide)", command=add_random_data).pack(side="left", padx=6)
ttk.Button(btn_frame, text="View Table", command=lambda: view_table_data(current_table.get())).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Help / Cheat Sheet", command=show_help).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Exit", command=root.destroy).pack(side="left", padx=5)

# Query frame (user can type any SQL)
# query_frame = ttk.LabelFrame(root, text="SQL Query Runner")
# query_frame.pack(fill="x", padx=8, pady=8)
# query_text = scrolledtext.ScrolledText(query_frame, height=6)
# query_text.pack(fill="x", padx=6, pady=6)
# ttk.Button(query_frame, text="Run SQL", command=execute_user_query).pack(padx=6, pady=6)

query_frame = tk.LabelFrame(root,text="Execute SQL Query")
query_frame.pack(fill=tk.X,padx=5,pady=5)
query_text = scrolledtext.ScrolledText(query_frame,height=4)
query_text.pack(fill=tk.X,padx=5,pady=5)
btn_exec = tk.Button(query_frame,text="Execute SQL",command=execute_user_query)
btn_exec.pack(side=tk.RIGHT,padx=5,pady=5)

# Results area
result_frame = ttk.Frame(root)
result_frame.pack(fill="both", expand=True, padx=8, pady=8)
result_tree = ttk.Treeview(result_frame)
result_tree.pack(fill="both", expand=True, side="left")

# add a simple vertical scrollbar for the treeview
vsb = ttk.Scrollbar(result_frame, orient="vertical", command=result_tree.yview)
vsb.pack(side="right", fill="y")
result_tree.configure(yscrollcommand=vsb.set)

# initialize table menu & default DB
update_table_menu_values(db_type_var.get())

# update table menu when DB selection changes
def on_db_change(*args):
    update_table_menu_values(db_type_var.get())

db_type_var.trace_add("write", on_db_change)

root.mainloop()
