import sqlite3
from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 

app = FastAPI() 

# Base Pydantic model for receiving data from requests
class Employee(BaseModel): 
    id: int 
    name: str
    department: str
    salary: float

# Helper function to connect to SQLite and return a dictionary-like cursor
def get_db_connection():
    conn = sqlite3.connect("employees.db")
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

# Create the tables if they don't exist when the app starts
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Employee table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)
    
    # Attendance tracking table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            employee_id INTEGER,
            attendance_count INTEGER DEFAULT 0,
            PRIMARY KEY (employee_id),
            FOREIGN KEY (employee_id) REFERENCES employees (id) ON DELETE CASCADE
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Management API!"}

@app.post("/employees") 
def add_employee(emp: Employee): 
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
            (emp.id, emp.name, emp.department, emp.salary)
        )
        cursor.execute("INSERT INTO attendance (employee_id, attendance_count) VALUES (?, 0)", (emp.id,))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    conn.close()
    return {"message": "Add employee", "data": emp} 

@app.get("/employees")  
def get_all_employees(): 
    conn = get_db_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM employees").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/employees/{id}") 
def get_employee_by_id(id: int):  
    conn = get_db_connection()
    cursor = conn.cursor()
    row = cursor.execute("SELECT * FROM employees WHERE id = ?", (id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Employee not found") 
    return dict(row)

@app.put("/employees/{id}") 
def update_employee(id: int, updated_employee: Employee):  
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if employee exists
    row = cursor.execute("SELECT id FROM employees WHERE id = ?", (id,)).fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found") 
    
    cursor.execute(
        "UPDATE employees SET name = ?, department = ?, salary = ? WHERE id = ?",
        (updated_employee.name, updated_employee.department, updated_employee.salary, id)
    )
    conn.commit()
    conn.close()
    return {"message": "Update employee", "data": updated_employee} 

@app.delete("/employees/{id}") 
def delete_employee(id: int): 
    conn = get_db_connection()
    cursor = conn.cursor()
    
    row = cursor.execute("SELECT * FROM employees WHERE id = ?", (id,)).fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found") 
    
    cursor.execute("DELETE FROM employees WHERE id = ?", (id,))
    cursor.execute("DELETE FROM attendance WHERE employee_id = ?", (id,))
    conn.commit()
    conn.close()
    return {"message": "Delete employee", "data": dict(row)} 

@app.get("/employees/department/{name}")
def get_employees_by_department(name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Using LOWER() to ensure case-insensitive matching like before
    rows = cursor.execute("SELECT * FROM employees WHERE LOWER(department) = LOWER(?)", (name,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.post("/attendance/{id}")
def mark_attendance(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    row = cursor.execute("SELECT id FROM employees WHERE id = ?", (id,)).fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found") 
        
    cursor.execute("UPDATE attendance SET attendance_count = attendance_count + 1 WHERE employee_id = ?", (id,))
    conn.commit()
    
    # Fetch updated record to return
    updated_row = cursor.execute("""
        SELECT e.id, e.name, a.attendance_count 
        FROM employees e 
        JOIN attendance a ON e.id = a.employee_id 
        WHERE e.id = ?
    """, (id,)).fetchone()
    
    conn.close()
    return {"message": "Mark attendance", "data": dict(updated_row)}

@app.get("/attendance")
def get_attendance_records():
    conn = get_db_connection()
    cursor = conn.cursor()
    rows = cursor.execute("""
        SELECT e.id, e.name, a.attendance_count 
        FROM employees e 
        JOIN attendance a ON e.id = a.employee_id
    """).fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/high-salary-employees")
def get_employees_with_high_salary():
    conn = get_db_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM employees WHERE salary > 50000").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/search-employee/{name}")
def search_employee_by_name(name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Uses SQL LIKE for wildcards (matches names containing the search term)
    rows = cursor.execute("SELECT * FROM employees WHERE LOWER(name) LIKE LOWER(?)", (f"%{name}%",)).fetchall()
    conn.close()
    return [dict(row) for row in rows]
