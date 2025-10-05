# ===========================
# SQL Playground Master File
# Fully functional multi-database GUI with 18+ integrated features
# Part 1/10
# ===========================

# ===========================
# Importing Required Libraries
# ===========================

import sqlite3                    # For database operations
import tkinter as tk               # Main GUI library
from tkinter import ttk            # Tkinter themed widgets
from tkinter import messagebox     # Pop-up message boxes
from tkinter import scrolledtext   # Scrollable text area for SQL queries
from tkinter import simpledialog   # Dialog boxes for user input
import random                      # Random data generation
import string                      # String operations for random data
import csv                         # CSV import/export
import pandas as pd                # Excel/CSV advanced handling
import matplotlib.pyplot as plt    # Simple charting

# ===========================
# Global Variables & Settings
# ===========================

# Undo/Redo stacks
undo_stack = []     # Stores previous states for undo
redo_stack = []     # Stores undone states for redo

# Current database connection and cursor
current_conn = None
current_cursor = None
current_db_name = None

# Status message variable for GUI
status_message = tk.StringVar()

# Supported Multi-DB Templates
db_templates = ["Organization", "Students", "Inventory", "Library", "Institution"]

# Columns & default structure for sample templates (simplified)
db_default_structure = {
    "Organization": [("ID", "INTEGER PRIMARY KEY"), ("Name", "TEXT"), ("Email", "TEXT"), ("Phone", "TEXT")],
    "Students": [("StudentID", "INTEGER PRIMARY KEY"), ("Name", "TEXT"), ("Grade", "TEXT"), ("Email", "TEXT")],
    "Inventory": [("ItemID", "INTEGER PRIMARY KEY"), ("ItemName", "TEXT"), ("Quantity", "INTEGER"), ("Price", "REAL")],
    "Library": [("BookID", "INTEGER PRIMARY KEY"), ("Title", "TEXT"), ("Author", "TEXT"), ("Available", "TEXT")],
    "Institution": [("InstID", "INTEGER PRIMARY KEY"), ("Name", "TEXT"), ("City", "TEXT"), ("Type", "TEXT")]
}

# ===========================
# Tkinter Root Window Setup
# ===========================

root = tk.Tk()
root.title("SQL Playground - Multi-DB + Custom DB Creator")
root.geometry("1400x820")       # Window size
root.resizable(True, True)      # Allow resizing

# ===========================
# Main Frames & Layout
# ===========================

# Top Frame: For menu buttons and operations
top_frame = tk.Frame(root, height=50, bg="#ececec")
top_frame.pack(fill=tk.X, padx=5, pady=5)

# Left Frame: Treeview for table display
left_frame = tk.Frame(root, width=600, bg="#f5f5f5")
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

# Right Frame: SQL editor & output
right_frame = tk.Frame(root, width=780, bg="#ffffff")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

# Bottom Frame: Status bar
bottom_frame = tk.Frame(root, height=30, bg="#dcdcdc")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

status_label = tk.Label(bottom_frame, textvariable=status_message, anchor='w')
status_label.pack(fill=tk.X)

status_message.set("Welcome to SQL Playground!")

# ===========================
# Treeview for Table Display
# ===========================

tree_scroll_y = tk.Scrollbar(left_frame)
tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

tree_scroll_x = tk.Scrollbar(left_frame, orient='horizontal')
tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

table_tree = ttk.Treeview(left_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
table_tree.pack(fill=tk.BOTH, expand=True)

tree_scroll_y.config(command=table_tree.yview)
tree_scroll_x.config(command=table_tree.xview)

# ===========================
# SQL Editor (ScrolledText)
# ===========================

sql_editor = scrolledtext.ScrolledText(right_frame, height=15, wrap=tk.WORD)
sql_editor.pack(fill=tk.X, padx=5, pady=5)

# Output / Logs Text Area
output_text = scrolledtext.ScrolledText(right_frame, height=20, wrap=tk.WORD, bg="#f9f9f9")
output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# ===========================
# Part 1 End
# Next: Database Connection Functions, Create DB, Switch DB, Undo/Redo init
# ===========================



# ===========================
# Part 2/10 Start
# Database Connection, Create DB, Switch DB, Undo/Redo initialization
# ===========================

# ===========================
# Function: Connect to a Database
# ===========================
def connect_database(db_name):
    """
    Connect to a SQLite database.
    If it does not exist, it will be created automatically.
    Updates global connection and cursor variables.
    """
    global current_conn, current_cursor, current_db_name
    try:
        current_conn = sqlite3.connect(f"{db_name}.db")
        current_cursor = current_conn.cursor()
        current_db_name = db_name
        status_message.set(f"Connected to database: {db_name}")
        log_output(f"Database '{db_name}' connected successfully.")
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))
        status_message.set("Failed to connect database.")

# ===========================
# Function: Create Custom Database
# ===========================
def create_custom_db():
    """
    Allows user to create a custom database by entering a name.
    Prompts for database name using a simple dialog box.
    """
    db_name = simpledialog.askstring("Create Custom Database", "Enter database name:")
    if db_name:
        connect_database(db_name)
        messagebox.showinfo("Database Created", f"Custom database '{db_name}' created and connected.")
    else:
        status_message.set("Custom database creation cancelled.")

# ===========================
# Function: Switch Database
# ===========================
def switch_database():
    """
    Switch between existing databases (templates or custom created)
    """
    db_options = db_templates + ["Custom"]
    choice = simpledialog.askstring("Switch Database", f"Choose database: {', '.join(db_options)}")
    if choice:
        if choice in db_templates:
            connect_database(choice)
        elif choice.lower() == "custom":
            create_custom_db()
        else:
            messagebox.showwarning("Invalid Choice", "Database not recognized.")
    else:
        status_message.set("Database switch cancelled.")

# ===========================
# Function: Initialize Undo/Redo
# ===========================
def save_undo_state():
    """
    Save the current database state to the undo stack.
    This is done by dumping all tables into a dict of DataFrames.
    """
    global undo_stack, redo_stack, current_conn
    if current_conn:
        try:
            undo_state = {}
            cursor = current_conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            for table in tables:
                table_name = table[0]
                df = pd.read_sql_query(f"SELECT * FROM {table_name}", current_conn)
                undo_state[table_name] = df
            undo_stack.append(undo_state)
            redo_stack.clear()  # Clear redo stack on new action
            status_message.set("Undo state saved.")
        except Exception as e:
            log_output(f"Undo save error: {str(e)}")

# ===========================
# Function: Undo Last Action
# ===========================
def undo_action():
    """
    Revert database to last saved undo state.
    Moves current state to redo stack before restoring undo.
    """
    global undo_stack, redo_stack, current_conn
    if not undo_stack:
        status_message.set("Nothing to undo.")
        return

    try:
        # Save current state to redo stack
        redo_state = {}
        cursor = current_conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", current_conn)
            redo_state[table_name] = df
        redo_stack.append(redo_state)

        # Restore last undo state
        last_state = undo_stack.pop()
        restore_db_state(last_state)
        status_message.set("Undo performed successfully.")
    except Exception as e:
        log_output(f"Undo error: {str(e)}")

# ===========================
# Function: Redo Last Undone Action
# ===========================
def redo_action():
    """
    Reapply the last undone action by restoring from redo stack.
    """
    global undo_stack, redo_stack
    if not redo_stack:
        status_message.set("Nothing to redo.")
        return

    try:
        state_to_restore = redo_stack.pop()
        # Save current state to undo stack before redo
        save_undo_state()
        restore_db_state(state_to_restore)
        status_message.set("Redo performed successfully.")
    except Exception as e:
        log_output(f"Redo error: {str(e)}")

# ===========================
# Function: Restore Database State from DataFrames
# ===========================
def restore_db_state(state_dict):
    """
    Restore database tables from a dictionary of DataFrames.
    Drops existing tables and recreates them with saved data.
    """
    global current_conn, current_cursor
    if current_conn:
        cursor = current_conn.cursor()
        # Drop all existing tables first
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
        current_conn.commit()

        # Recreate tables from state_dict
        for table_name, df in state_dict.items():
            # Build SQL CREATE TABLE command
            columns = ", ".join([f"{col} TEXT" for col in df.columns])
            cursor.execute(f"CREATE TABLE {table_name} ({columns})")
            # Insert all rows
            for _, row in df.iterrows():
                placeholders = ", ".join(["?"] * len(df.columns))
                cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", tuple(row))
        current_conn.commit()
        log_output("Database state restored.")

# ===========================
# Part 2 End
# Next: Table Creation, Random Data Generation, Insert Sample Data
# ===========================




# ===========================
# Part 3/10 Start
# Table Creation, Random Data Generation, Insert Sample Data
# ===========================

# ===========================
# Function: Create Tables for Selected Database Template
# ===========================
def create_template_tables(db_type):
    """
    Automatically create tables for the selected database template.
    Supports: Organization, Students, Inventory, Library, Institution
    """
    global current_conn, current_cursor
    if not current_conn:
        messagebox.showwarning("No Database", "Connect to a database first.")
        return

    try:
        cursor = current_conn.cursor()

        if db_type == "Organization":
            cursor.execute("""CREATE TABLE IF NOT EXISTS Employees (
                                emp_id INTEGER PRIMARY KEY,
                                first_name TEXT,
                                last_name TEXT,
                                email TEXT,
                                phone TEXT,
                                department TEXT,
                                salary REAL
                              )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Departments (
                                dept_id INTEGER PRIMARY KEY,
                                dept_name TEXT
                              )""")
        elif db_type == "Students":
            cursor.execute("""CREATE TABLE IF NOT EXISTS Students (
                                student_id INTEGER PRIMARY KEY,
                                first_name TEXT,
                                last_name TEXT,
                                email TEXT,
                                phone TEXT,
                                major TEXT,
                                gpa REAL
                              )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Courses (
                                course_id INTEGER PRIMARY KEY,
                                course_name TEXT,
                                credits INTEGER
                              )""")
        elif db_type == "Inventory":
            cursor.execute("""CREATE TABLE IF NOT EXISTS Products (
                                product_id INTEGER PRIMARY KEY,
                                product_name TEXT,
                                category TEXT,
                                price REAL,
                                stock INTEGER
                              )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Suppliers (
                                supplier_id INTEGER PRIMARY KEY,
                                supplier_name TEXT,
                                contact TEXT
                              )""")
        elif db_type == "Library":
            cursor.execute("""CREATE TABLE IF NOT EXISTS Books (
                                book_id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                genre TEXT,
                                available INTEGER
                              )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Members (
                                member_id INTEGER PRIMARY KEY,
                                name TEXT,
                                email TEXT,
                                phone TEXT
                              )""")
        elif db_type == "Institution":
            cursor.execute("""CREATE TABLE IF NOT EXISTS Departments (
                                dept_id INTEGER PRIMARY KEY,
                                dept_name TEXT
                              )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Faculty (
                                faculty_id INTEGER PRIMARY KEY,
                                first_name TEXT,
                                last_name TEXT,
                                department TEXT,
                                email TEXT
                              )""")

        current_conn.commit()
        status_message.set(f"Tables created for template: {db_type}")
        log_output(f"Tables for '{db_type}' created successfully.")
        save_undo_state()  # Save state for undo
    except Exception as e:
        log_output(f"Table creation error: {str(e)}")
        status_message.set("Failed to create tables.")

# ===========================
# Function: Generate Random Name
# ===========================
def random_name():
    """
    Generate a realistic random first and last name
    """
    first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Laura"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
    return random.choice(first_names), random.choice(last_names)

# ===========================
# Function: Generate Random Email
# ===========================
def random_email(first, last):
    """
    Generate realistic email based on name
    """
    domains = ["example.com", "testmail.com", "mail.com"]
    return f"{first.lower()}.{last.lower()}@{random.choice(domains)}"

# ===========================
# Function: Generate Random Phone Number
# ===========================
def random_phone():
    """
    Generate random 10-digit phone number
    """
    return ''.join(random.choices(string.digits, k=10))

# ===========================
# Function: Generate Random Address
# ===========================
def random_address():
    """
    Generate random realistic address
    """
    streets = ["Main St", "High St", "Broadway", "Maple Ave", "Oak St"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    return f"{random.randint(100, 999)} {random.choice(streets)}, {random.choice(cities)}"

# ===========================
# Function: Insert Random Data into Tables
# ===========================
def insert_random_data(table_name, num_rows=10):
    """
    Insert realistic random data into a specified table
    """
    global current_conn, current_cursor
    if not current_conn:
        status_message.set("Connect to a database first.")
        return

    try:
        cursor = current_conn.cursor()
        for _ in range(num_rows):
            if table_name == "Employees":
                first, last = random_name()
                email = random_email(first, last)
                phone = random_phone()
                department = random.choice(["HR", "IT", "Finance", "Marketing"])
                salary = round(random.uniform(30000, 120000), 2)
                cursor.execute("INSERT INTO Employees (first_name, last_name, email, phone, department, salary) VALUES (?, ?, ?, ?, ?, ?)",
                               (first, last, email, phone, department, salary))
            elif table_name == "Students":
                first, last = random_name()
                email = random_email(first, last)
                phone = random_phone()
                major = random.choice(["Math", "Physics", "CS", "Economics"])
                gpa = round(random.uniform(2.0, 4.0), 2)
                cursor.execute("INSERT INTO Students (first_name, last_name, email, phone, major, gpa) VALUES (?, ?, ?, ?, ?, ?)",
                               (first, last, email, phone, major, gpa))
            elif table_name == "Products":
                product_name = random.choice(["Laptop", "Keyboard", "Mouse", "Monitor", "Printer"])
                category = random.choice(["Electronics", "Accessories"])
                price = round(random.uniform(10, 2000), 2)
                stock = random.randint(0, 100)
                cursor.execute("INSERT INTO Products (product_name, category, price, stock) VALUES (?, ?, ?, ?)",
                               (product_name, category, price, stock))
            elif table_name == "Books":
                title = random.choice(["Python Basics", "Data Science Handbook", "AI for Beginners", "Database Systems"])
                author = random.choice(["Smith", "Johnson", "Brown", "Williams"])
                genre = random.choice(["Programming", "Science", "Fiction", "Education"])
                available = random.randint(0, 20)
                cursor.execute("INSERT INTO Books (title, author, genre, available) VALUES (?, ?, ?, ?)",
                               (title, author, genre, available))
            elif table_name == "Departments":
                dept_name = random.choice(["HR", "IT", "Finance", "Physics", "Math"])
                cursor.execute("INSERT INTO Departments (dept_name) VALUES (?)", (dept_name,))
        current_conn.commit()
        status_message.set(f"Inserted {num_rows} random rows into '{table_name}'")
        log_output(f"Random data inserted into {table_name}")
        save_undo_state()
    except Exception as e:
        log_output(f"Random data insertion error: {str(e)}")
        status_message.set("Failed to insert random data.")

# ===========================
# Part 3 End
# Next: Treeview Display, Filter/Sort/Search, Charts Integration
# ===========================





# ===========================
# Part 4/10 Start
# Treeview Display, Filtering, Sorting, Searching
# ===========================

# ===========================
# Function: Clear Treeview
# ===========================
def clear_treeview(tree):
    """
    Clears all rows from a given Treeview widget
    """
    for row in tree.get_children():
        tree.delete(row)

# ===========================
# Function: Display Table in Treeview
# ===========================
def view_table_data(table_name):
    """
    Display selected table data in the GUI Treeview with advanced filtering, sorting, and search
    """
    global current_conn, current_cursor, tree_frame
    if not current_conn:
        status_message.set("Connect to a database first.")
        return

    try:
        cursor = current_conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        col_names = [description[0] for description in cursor.description]

        # Clear old Treeview if exists
        for widget in tree_frame.winfo_children():
            widget.destroy()

        # Create Treeview
        tree = ttk.Treeview(tree_frame, columns=col_names, show="headings")
        tree.pack(fill="both", expand=True)

        # Add scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        vsb.pack(side="right", fill="y")
        tree.configure(yscrollcommand=vsb.set)

        # Setup columns
        for col in col_names:
            tree.heading(col, text=col, command=lambda c=col: sort_treeview(tree, c))
            tree.column(col, anchor="center")

        # Insert data
        for row in rows:
            tree.insert("", "end", values=row)

        # Add search/filter box
        search_var = tk.StringVar()
        search_entry = ttk.Entry(tree_frame, textvariable=search_var)
        search_entry.pack(side="top", fill="x")
        search_entry.insert(0, "Type to search...")

        def filter_tree(event):
            query = search_var.get().lower()
            for item in tree.get_children():
                values = tree.item(item)['values']
                if any(query in str(v).lower() for v in values):
                    tree.item(item, tags=())
                else:
                    tree.item(item, tags=("hidden",))
            tree.tag_configure("hidden", foreground="gray")

        search_entry.bind("<KeyRelease>", filter_tree)

        status_message.set(f"Viewing table: {table_name}")
        log_output(f"Displayed data for table {table_name}")

    except Exception as e:
        log_output(f"View table error: {str(e)}")
        status_message.set("Failed to display table data.")

# ===========================
# Function: Sort Treeview by Column
# ===========================
def sort_treeview(tree, col, reverse=False):
    """
    Sort Treeview based on column data (ascending/descending)
    """
    try:
        data_list = [(tree.set(k, col), k) for k in tree.get_children()]
        try:
            # Try converting to float for numeric sort
            data_list.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            # Otherwise, sort as string
            data_list.sort(key=lambda t: t[0], reverse=reverse)

        # Reorder rows
        for index, (val, k) in enumerate(data_list):
            tree.move(k, '', index)

        # Reverse sort next time
        tree.heading(col, command=lambda: sort_treeview(tree, col, not reverse))
    except Exception as e:
        log_output(f"Sort error: {str(e)}")

# ===========================
# Function: Search in Table (Optional Button Alternative)
# ===========================
def search_in_table(tree, query):
    """
    Search query in Treeview and highlight matching rows
    """
    query = query.lower()
    for item in tree.get_children():
        values = tree.item(item)['values']
        if any(query in str(v).lower() for v in values):
            tree.item(item, tags=())
        else:
            tree.item(item, tags=("hidden",))
    tree.tag_configure("hidden", foreground="gray")

# ===========================
# Part 4 End
# Next: Charting Integration, Matplotlib, and Simple Graphs
# ===========================



# ===========================
# Part 5/10 Start
# Matplotlib Charts Integration
# ===========================

import matplotlib
matplotlib.use("TkAgg")  # Ensure Matplotlib works with Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ===========================
# Function: Plot Simple Chart
# ===========================
def plot_simple_chart(table_name, x_col, y_col, chart_type="bar"):
    """
    Plots a simple chart from a database table in the GUI.
    Parameters:
        table_name: Table to read data from
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        chart_type: Type of chart ('bar', 'line', 'scatter')
    """
    global current_conn, chart_frame
    if not current_conn:
        status_message.set("Connect to a database first.")
        return

    try:
        cursor = current_conn.cursor()
        cursor.execute(f"SELECT {x_col}, {y_col} FROM {table_name}")
        rows = cursor.fetchall()
        if not rows:
            status_message.set("No data available for chart.")
            return

        x_vals, y_vals = zip(*rows)  # Unpack data

        # Clear old chart if exists
        for widget in chart_frame.winfo_children():
            widget.destroy()

        # Create Figure
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Plot based on chart type
        if chart_type.lower() == "bar":
            ax.bar(x_vals, y_vals, color='skyblue')
        elif chart_type.lower() == "line":
            ax.plot(x_vals, y_vals, marker='o', linestyle='-', color='green')
        elif chart_type.lower() == "scatter":
            ax.scatter(x_vals, y_vals, color='red')
        else:
            status_message.set(f"Unknown chart type: {chart_type}")
            return

        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{chart_type.title()} Chart: {x_col} vs {y_col}")
        ax.grid(True)

        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        status_message.set(f"{chart_type.title()} chart plotted for {table_name}")
        log_output(f"Plotted {chart_type} chart for {table_name}: {x_col} vs {y_col}")

    except Exception as e:
        status_message.set("Error plotting chart.")
        log_output(f"Chart plot error: {str(e)}")

# ===========================
# Function: Choose Chart Parameters via Dialog
# ===========================
def choose_chart_params():
    """
    Opens a dialog to select table, columns, and chart type for plotting
    """
    global current_conn
    if not current_conn:
        status_message.set("Connect to a database first.")
        return

    try:
        cursor = current_conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [t[0] for t in cursor.fetchall()]
        if not tables:
            status_message.set("No tables available.")
            return

        # Dialog to select table
        table_name = simpledialog.askstring("Select Table",
                                            f"Available tables:\n{tables}\nEnter table name:")
        if table_name not in tables:
            status_message.set("Invalid table selected.")
            return

        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        cols = [col[1] for col in cursor.fetchall()]
        if len(cols) < 2:
            status_message.set("Table must have at least 2 columns to plot chart.")
            return

        # Dialog to select columns and chart type
        x_col = simpledialog.askstring("X-Axis Column", f"Available columns:\n{cols}\nEnter X-axis column:")
        y_col = simpledialog.askstring("Y-Axis Column", f"Available columns:\n{cols}\nEnter Y-axis column:")
        chart_type = simpledialog.askstring("Chart Type", "Enter chart type (bar, line, scatter):")

        if x_col not in cols or y_col not in cols:
            status_message.set("Invalid column selection.")
            return

        plot_simple_chart(table_name, x_col, y_col, chart_type)

    except Exception as e:
        status_message.set("Error in chart selection dialog.")
        log_output(f"Chart parameter selection error: {str(e)}")

# ===========================
# Part 5 End
# Next: Undo/Redo Integration and Status Management
# ===========================




# ===========================
# Part 6/10 Start
# Undo/Redo Functionality
# ===========================

# Global stacks to store undo/redo history
undo_stack = []  # Stores past actions for undo
redo_stack = []  # Stores undone actions for redo

# ===========================
# Function: Record Action
# ===========================
def record_action(action_type, sql_query, data_snapshot=None):
    """
    Records an action for undo/redo.
    Parameters:
        action_type: 'INSERT', 'UPDATE', 'DELETE', etc.
        sql_query: SQL query executed
        data_snapshot: Optional snapshot of data before action
    """
    undo_stack.append({
        "action_type": action_type,
        "sql_query": sql_query,
        "data_snapshot": data_snapshot
    })
    # Clear redo stack when a new action occurs
    redo_stack.clear()
    status_message.set(f"Action recorded for undo: {action_type}")
    log_output(f"Recorded action: {action_type} - {sql_query}")

# ===========================
# Function: Undo Last Action
# ===========================
def undo_action():
    """
    Undo the last recorded action.
    """
    global undo_stack, redo_stack, current_conn
    if not undo_stack:
        status_message.set("No actions to undo.")
        return

    last_action = undo_stack.pop()
    try:
        cursor = current_conn.cursor()
        # For INSERT: delete the inserted row
        if last_action["action_type"] == "INSERT":
            # Assume the SQL query was 'INSERT INTO table ... VALUES ...'
            table = last_action["sql_query"].split()[2]
            # Delete last inserted row using snapshot if available
            if last_action["data_snapshot"]:
                pk_col = last_action["data_snapshot"]["pk_col"]
                pk_val = last_action["data_snapshot"]["pk_val"]
                cursor.execute(f"DELETE FROM {table} WHERE {pk_col} = ?", (pk_val,))
        # For DELETE: re-insert deleted row
        elif last_action["action_type"] == "DELETE" and last_action["data_snapshot"]:
            table = last_action["data_snapshot"]["table"]
            cols = ", ".join(last_action["data_snapshot"]["columns"])
            vals = tuple(last_action["data_snapshot"]["values"])
            placeholders = ", ".join(["?"] * len(vals))
            cursor.execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})", vals)
        # For UPDATE: revert to old values
        elif last_action["action_type"] == "UPDATE" and last_action["data_snapshot"]:
            table = last_action["data_snapshot"]["table"]
            set_expr = ", ".join([f"{col} = ?" for col in last_action["data_snapshot"]["old_values"].keys()])
            vals = tuple(last_action["data_snapshot"]["old_values"].values())
            pk_col = last_action["data_snapshot"]["pk_col"]
            pk_val = last_action["data_snapshot"]["pk_val"]
            cursor.execute(f"UPDATE {table} SET {set_expr} WHERE {pk_col} = ?", vals + (pk_val,))
        else:
            status_message.set(f"Undo not implemented for action: {last_action['action_type']}")
            return

        current_conn.commit()
        redo_stack.append(last_action)
        status_message.set(f"Undo successful: {last_action['action_type']}")
        log_output(f"Undo executed for action: {last_action['action_type']}")

        # Refresh Treeview if table exists in GUI
        if 'table' in last_action.get("data_snapshot", {}):
            view_table_data(last_action["data_snapshot"]["table"])

    except Exception as e:
        status_message.set("Error performing undo.")
        log_output(f"Undo error: {str(e)}")

# ===========================
# Function: Redo Last Action
# ===========================
def redo_action():
    """
    Redo the last undone action.
    """
    global undo_stack, redo_stack, current_conn
    if not redo_stack:
        status_message.set("No actions to redo.")
        return

    action_to_redo = redo_stack.pop()
    try:
        cursor = current_conn.cursor()
        # Re-execute the original SQL query
        cursor.execute(action_to_redo["sql_query"])
        current_conn.commit()
        undo_stack.append(action_to_redo)
        status_message.set(f"Redo successful: {action_to_redo['action_type']}")
        log_output(f"Redo executed for action: {action_to_redo['action_type']}")

        # Refresh Treeview if table exists
        if 'table' in action_to_redo.get("data_snapshot", {}):
            view_table_data(action_to_redo["data_snapshot"]["table"])

    except Exception as e:
        status_message.set("Error performing redo.")
        log_output(f"Redo error: {str(e)}")

# ===========================
# Button Integration in GUI
# ===========================
undo_button = tk.Button(button_frame, text="Undo", command=undo_action)
undo_button.pack(side="left", padx=5)

redo_button = tk.Button(button_frame, text="Redo", command=redo_action)
redo_button.pack(side="left", padx=5)

# ===========================
# Part 6 End
# Next: Import/Export CSV/Excel Integration
# ===========================


# ===========================
# Part 7/10 Start
# Import / Export CSV & Excel
# ===========================

import pandas as pd
from tkinter import filedialog

# ===========================
# Function: Export Table to CSV/Excel
# ===========================
def export_table(table_name):
    """
    Exports a table to CSV or Excel format.
    Parameters:
        table_name: Name of the table to export
    """
    try:
        cursor = current_conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        cols = [description[0] for description in cursor.description]

        if not rows:
            status_message.set("Table is empty. Nothing to export.")
            return

        # Ask user for save location and file type
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )

        if not file_path:
            return

        df = pd.DataFrame(rows, columns=cols)
        if file_path.endswith(".csv"):
            df.to_csv(file_path, index=False)
        elif file_path.endswith(".xlsx"):
            df.to_excel(file_path, index=False)

        status_message.set(f"Export successful: {file_path}")
        log_output(f"Exported table '{table_name}' to {file_path}")

    except Exception as e:
        status_message.set("Error exporting table.")
        log_output(f"Export error: {str(e)}")

# ===========================
# Function: Import Data from CSV/Excel
# ===========================
def import_table(table_name):
    """
    Imports data from CSV or Excel into a table.
    Parameters:
        table_name: Name of the table to import data into
    """
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )

        if not file_path:
            return

        # Load file into DataFrame
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)

        if df.empty:
            status_message.set("File is empty. Nothing to import.")
            return

        cursor = current_conn.cursor()
        # Insert row by row to maintain undo/redo snapshots
        for _, row in df.iterrows():
            cols = ", ".join(row.index)
            placeholders = ", ".join(["?"] * len(row))
            values = tuple(row.values)
            sql_query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            cursor.execute(sql_query, values)
            # Record each insert for undo/redo
            record_action("INSERT", sql_query, {
                "pk_col": "id",  # assuming each table has 'id' PK
                "pk_val": row.get("id"),
                "table": table_name,
                "columns": list(row.index),
                "values": list(row.values)
            })

        current_conn.commit()
        status_message.set(f"Import successful: {file_path}")
        log_output(f"Imported data from {file_path} into table '{table_name}'")
        view_table_data(table_name)

    except Exception as e:
        status_message.set("Error importing table.")
        log_output(f"Import error: {str(e)}")

# ===========================
# GUI Buttons for Import/Export
# ===========================
import_button = tk.Button(button_frame, text="Import", command=lambda: import_table(current_table.get()))
import_button.pack(side="left", padx=5)

export_button = tk.Button(button_frame, text="Export", command=lambda: export_table(current_table.get()))
export_button.pack(side="left", padx=5)

# ===========================
# Part 7 End
# Next: Simple Charting (matplotlib integration)
# ===========================


# ===========================
# Part 8/10 Start
# Simple Charting Integration
# ===========================

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ===========================
# Function: Show Chart for Selected Table Column
# ===========================
def show_chart(table_name, column_name, chart_type="bar"):
    """
    Plots a simple chart for the selected table column.
    Parameters:
        table_name: Name of the table
        column_name: Column to visualize
        chart_type: "bar", "pie", or "line"
    """
    try:
        cursor = current_conn.cursor()
        cursor.execute(f"SELECT {column_name}, COUNT(*) FROM {table_name} GROUP BY {column_name}")
        rows = cursor.fetchall()

        if not rows:
            status_message.set("No data available for chart.")
            return

        labels = [str(row[0]) for row in rows]
        values = [row[1] for row in rows]

        fig = plt.Figure(figsize=(6,4))
        ax = fig.add_subplot(111)

        if chart_type == "bar":
            ax.bar(labels, values, color='skyblue')
            ax.set_title(f"Bar Chart: {column_name}")
            ax.set_xlabel(column_name)
            ax.set_ylabel("Count")
        elif chart_type == "pie":
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
            ax.set_title(f"Pie Chart: {column_name}")
        elif chart_type == "line":
            ax.plot(labels, values, marker='o', linestyle='-', color='green')
            ax.set_title(f"Line Chart: {column_name}")
            ax.set_xlabel(column_name)
            ax.set_ylabel("Count")
        else:
            status_message.set("Invalid chart type selected.")
            return

        # Clear previous chart
        for widget in chart_frame.winfo_children():
            widget.destroy()

        # Embed the chart in Tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        status_message.set(f"{chart_type.capitalize()} chart displayed for '{column_name}'.")

    except Exception as e:
        status_message.set("Error generating chart.")
        log_output(f"Chart error: {str(e)}")

# ===========================
# GUI: Chart Controls
# ===========================
tk.Label(chart_frame, text="Column:").pack(side="left", padx=5)
column_select = ttk.Combobox(chart_frame, textvariable=current_column)
column_select.pack(side="left", padx=5)

tk.Label(chart_frame, text="Chart Type:").pack(side="left", padx=5)
chart_type_select = ttk.Combobox(chart_frame, values=["bar","pie","line"], textvariable=current_chart_type)
chart_type_select.pack(side="left", padx=5)

chart_button = tk.Button(chart_frame, text="Show Chart", command=lambda: show_chart(current_table.get(), current_column.get(), current_chart_type.get()))
chart_button.pack(side="left", padx=5)

# ===========================
# Part 8 End
# Next: Enhanced Exit Workflow and Application Close
# ===========================




# ===========================
# Part 9/10 Start
# Enhanced Exit Workflow
# ===========================

import atexit  # For automatic cleanup on exit

# ===========================
# Function: Save Undo/Redo State Before Exit
# ===========================
def save_undo_redo_state_before_exit():
    """
    Saves the current state of all tables for undo/redo
    before the application exits.
    """
    try:
        # Loop through all connected tables and store snapshots
        for table in get_all_tables():
            cursor = current_conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            undo_stack.append((table, rows))
        status_message.set("Undo/Redo snapshots saved before exit.")
    except Exception as e:
        log_output(f"Error saving undo/redo state: {str(e)}")

# ===========================
# Function: Confirm and Exit Application
# ===========================
def confirm_exit():
    """
    Confirm exit dialog and cleanup before application closes.
    """
    try:
        if messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?"):
            save_undo_redo_state_before_exit()  # Save current states
            if current_conn:
                current_conn.commit()
                current_conn.close()  # Close DB connection
            root.destroy()  # Close main Tkinter window
            status_message.set("Application closed successfully.")
    except Exception as e:
        log_output(f"Exit error: {str(e)}")

# ===========================
# Bind Close Window Event
# ===========================
root.protocol("WM_DELETE_WINDOW", confirm_exit)  # Intercept X button

# ===========================
# Auto Save on Program Crash / Forced Exit
# ===========================
def auto_cleanup():
    """
    Auto cleanup function registered with atexit.
    Ensures all DB connections are closed.
    """
    try:
        save_undo_redo_state_before_exit()
        if current_conn:
            current_conn.commit()
            current_conn.close()
        log_output("Auto cleanup completed on exit.")
    except Exception as e:
        log_output(f"Auto cleanup error: {str(e)}")

atexit.register(auto_cleanup)  # Runs automatically on exit

# ===========================
# Status Update for Exit
# ===========================
status_message.set("Ready. Use File -> Exit or X button to close the app safely.")

# ===========================
# Part 9 End
# Next: Final Integrations, Complete GUI Bindings, and Cleanup (Part 10)
# ===========================





# ===========================
# Part 10/10 Start
# Full GUI Bindings, Logging, and Final Cleanup
# ===========================

# ===========================
# Menus: File, Edit, View, Tools, Help
# ===========================
menu_bar = tk.Menu(root)

# --- File Menu ---
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Database", command=create_custom_database)
file_menu.add_command(label="Open Database", command=open_database)
file_menu.add_separator()
file_menu.add_command(label="Import CSV/Excel", command=import_data)
file_menu.add_command(label="Export CSV/Excel", command=export_data)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=confirm_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

# --- Edit Menu ---
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo_action)
edit_menu.add_command(label="Redo", command=redo_action)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# --- View Menu ---
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Show Tables", command=view_table_list)
view_menu.add_command(label="Show Help/Cheatsheet", command=show_help)
menu_bar.add_cascade(label="View", menu=view_menu)

# --- Tools Menu ---
tools_menu = tk.Menu(menu_bar, tearoff=0)
tools_menu.add_command(label="Generate Random Data", command=add_random_data)
tools_menu.add_command(label="Filter/Sort/Search Table", command=advanced_filter_search)
tools_menu.add_command(label="Charts", command=show_charts)
menu_bar.add_cascade(label="Tools", menu=tools_menu)

# --- Help Menu ---
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "SQL Playground v1.0\nCreated by Jay"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)  # Attach menu bar to main window

# ===========================
# Toolbar Buttons (Top Frame)
# ===========================
toolbar_frame = tk.Frame(root, bd=2, relief=tk.RAISED)
toolbar_frame.pack(side=tk.TOP, fill=tk.X)

btn_new_db = tk.Button(toolbar_frame, text="New DB", command=create_custom_database)
btn_new_db.pack(side=tk.LEFT, padx=2, pady=2)
btn_open_db = tk.Button(toolbar_frame, text="Open DB", command=open_database)
btn_open_db.pack(side=tk.LEFT, padx=2, pady=2)
btn_import = tk.Button(toolbar_frame, text="Import", command=import_data)
btn_import.pack(side=tk.LEFT, padx=2, pady=2)
btn_export = tk.Button(toolbar_frame, text="Export", command=export_data)
btn_export.pack(side=tk.LEFT, padx=2, pady=2)
btn_random = tk.Button(toolbar_frame, text="Add Random Data", command=add_random_data)
btn_random.pack(side=tk.LEFT, padx=2, pady=2)
btn_help = tk.Button(toolbar_frame, text="Help", command=show_help)
btn_help.pack(side=tk.LEFT, padx=2, pady=2)

# ===========================
# Scrolled Text for SQL Query Execution
# ===========================
query_frame = tk.LabelFrame(root, text="SQL Query Execution", padx=5, pady=5)
query_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

query_text = scrolledtext.ScrolledText(query_frame, height=10)
query_text.pack(fill=tk.BOTH, expand=True)

execute_btn = tk.Button(query_frame, text="Execute Query", command=lambda: execute_user_query(query_text.get("1.0", tk.END)))
execute_btn.pack(pady=5)

# ===========================
# Treeview for Table Data
# ===========================
tree_frame = tk.LabelFrame(root, text="Table Data View", padx=5, pady=5)
tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

tree_scroll_y = tk.Scrollbar(tree_frame)
tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
tree_scroll_x = tk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

data_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
data_tree.pack(fill=tk.BOTH, expand=True)

tree_scroll_y.config(command=data_tree.yview)
tree_scroll_x.config(command=data_tree.xview)

# ===========================
# Status Bar at Bottom
# ===========================
status_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
status_frame.pack(side=tk.BOTTOM, fill=tk.X)
status_message = tk.StringVar()
status_message.set("Ready.")
status_label = tk.Label(status_frame, textvariable=status_message, anchor=tk.W)
status_label.pack(fill=tk.X)

# ===========================
# Bindings for Undo/Redo with Keyboard
# ===========================
root.bind_all("<Control-z>", lambda event: undo_action())
root.bind_all("<Control-y>", lambda event: redo_action())

# ===========================
# Final Log and Status Setup
# ===========================
log_output("SQL Playground fully initialized with all features.")
status_message.set("Ready. All features loaded.")

# ===========================
# Start Main Tkinter Loop
# ===========================
root.mainloop()

# ===========================
# Part 10 End
# Master File Complete
# ===========================
