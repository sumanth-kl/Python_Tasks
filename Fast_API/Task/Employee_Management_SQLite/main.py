from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func, desc
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import IntegrityError

# --- DATABASE SETUP ---
DATABASE_URL = "sqlite:///./employees.db"

# connect_args={"check_same_thread": False} is required only for SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- SQLALCHEMY MODELS ---
class DBEmployee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

class DBAttendance(Base):
    __tablename__ = "attendance"
    
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), primary_key=True)
    attendance_count = Column(Integer, default=0)

# Create tables automatically
Base.metadata.create_all(bind=engine)

# --- FASTAPI SETUP ---
app = FastAPI()

# Dependency to get the database session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- PYDANTIC MODELS (SCHEMAS) ---
class EmployeeSchema(BaseModel): 
    id: int 
    name: str
    department: str
    salary: float

    class Config:
        from_attributes = True

# --- ENDPOINTS ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Management API!"}

@app.post("/employees", response_model=dict) 
def add_employee(emp: EmployeeSchema, db: Session = Depends(get_db)): 
    new_employee = DBEmployee(id=emp.id, name=emp.name, department=emp.department, salary=emp.salary)
    new_attendance = DBAttendance(employee_id=emp.id, attendance_count=0)
    
    try:
        db.add(new_employee)
        db.add(new_attendance)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    return {"message": "Add employee", "data": emp} 

@app.get("/employees")  
def get_all_employees(db: Session = Depends(get_db)): 
    employees = db.query(DBEmployee).all()
    return employees

@app.get("/employees/{id}") 
def get_employee_by_id(id: int, db: Session = Depends(get_db)):  
    employee = db.query(DBEmployee).filter(DBEmployee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found") 
    return employee

@app.put("/employees/{id}") 
def update_employee(id: int, updated_employee: EmployeeSchema, db: Session = Depends(get_db)):  
    employee = db.query(DBEmployee).filter(DBEmployee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found") 
    
    employee.name = updated_employee.name
    employee.department = updated_employee.department
    employee.salary = updated_employee.salary
    
    db.commit()
    return {"message": "Update employee", "data": updated_employee} 

@app.delete("/employees/{id}") 
def delete_employee(id: int, db: Session = Depends(get_db)): 
    employee = db.query(DBEmployee).filter(DBEmployee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found") 
    
    # Capture data before deleting to return it in the response
    deleted_data = {
        "id": employee.id,
        "name": employee.name,
        "department": employee.department,
        "salary": employee.salary
    }
    
    # Attendance row will automatically delete if foreign key ON DELETE CASCADE is configured at DB level,
    # but manually deleting guarantees it for standard SQLite setups.
    db.query(DBAttendance).filter(DBAttendance.employee_id == id).delete()
    db.delete(employee)
    db.commit()
    
    return {"message": "Delete employee", "data": deleted_data} 

@app.get("/employees/department/{name}")
def get_employees_by_department(name: str, db: Session = Depends(get_db)):
    employees = db.query(DBEmployee).filter(func.lower(DBEmployee.department) == func.lower(name)).all()
    return employees

@app.post("/attendance/{id}")
def mark_attendance(id: int, db: Session = Depends(get_db)):
    employee = db.query(DBEmployee).filter(DBEmployee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found") 
        
    attendance = db.query(DBAttendance).filter(DBAttendance.employee_id == id).first()
    if attendance:
        attendance.attendance_count += 1
    else:
        attendance = DBAttendance(employee_id=id, attendance_count=1)
        db.add(attendance)
        
    db.commit()
    
    return {
        "message": "Mark attendance", 
        "data": {
            "id": employee.id,
            "name": employee.name,
            "attendance_count": attendance.attendance_count
        }
    }

@app.get("/attendance")
def get_attendance_records(db: Session = Depends(get_db)):
    records = db.query(
        DBEmployee.id, 
        DBEmployee.name, 
        DBAttendance.attendance_count
    ).join(DBAttendance, DBEmployee.id == DBAttendance.employee_id).all()
    
    # Map the tuple results into dictionaries for JSON response
    return [{"id": r.id, "name": r.name, "attendance_count": r.attendance_count} for r in records]

@app.get("/high-salary-employees")
def get_employees_with_high_salary(db: Session = Depends(get_db)):
    # Sort by salary from highest to lowest and take the first record
    employee = db.query(DBEmployee).order_by(desc(DBEmployee.salary)).first()
    
    if not employee:
        raise HTTPException(status_code=404, detail="No employees found")
        
    return employee

@app.get("/search-employee/{name}")
def search_employee_by_name(name: str, db: Session = Depends(get_db)):
    search_term = f"%{name}%"
    employees = db.query(DBEmployee).filter(func.lower(DBEmployee.name).like(func.lower(search_term))).all()
    return employees
