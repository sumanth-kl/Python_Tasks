# ============================================================
# 📝 FastAPI Employee Management App (CRUD) - MySQL Database Version
# pip install fastapi uvicorn sqlalchemy pymysql
# ============================================================

from datetime import datetime, timezone
from typing import List
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy import create_engine, CheckConstraint, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Session, relationship
from typing import Literal, Optional
from fastapi.responses import PlainTextResponse

# ------------------------------------------------------------
# 🚀 Create FastAPI App
# ------------------------------------------------------------
app = FastAPI(title="Employee Management API")

# ------------------------------------------------------------
# 🗄️ Database Configuration (MySQL)
# ------------------------------------------------------------
# Replace with your actual database user, password, host, and database name
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/company_db"

engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True,  # Automatically checks and repairs broken connections
    pool_recycle=3600    # Prevents "MySQL server has gone away" errors by recycling connections
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DB Dependency injection helper
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------

# For adding or updating an employee
class EmployeeCreate(BaseModel):
    emp_name: str
    emp_dprt: str
    emp_dsgn: str
    emp_atdnce: Literal["present", "leave"] # ✅ Rejects any string except these two
    leave_reason: Optional[str] = None      # ✅ New column for leave notes
    emp_sal: float

# For returning complete employee details
class EmployeeResponse(BaseModel):
    emp_id: int
    emp_name: str
    emp_dprt: str
    emp_dsgn: str
    date_time: datetime
    emp_atdnce: str
    leave_reason: Optional[str]
    emp_joindt: datetime
    emp_sal: float

    class Config:
        from_attributes = True

# For returning attendance details
class AttendanceResponse(BaseModel):
    emp_id: int
    emp_name: str
    emp: int
    emp_atdnce: Literal["present", "leave"]
    leave_reason: Optional[str]

    class Config:
        from_attributes = True

# This wrapper allows your function to return {"message": "...", "data": ...}
class AttendancePostResponseWrapper(BaseModel):
    message: str
    data: AttendanceResponse  # Reuses your existing AttendanceResponse model

    class Config:
        from_attributes = True

# ------------------------------------------------------------
# 🗄️ SQLAlchemy Database Models
# ------------------------------------------------------------

class EmployeeDetail(Base):
    __tablename__ = "employee_details"

    emp_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    emp_name = Column(String(100), nullable=False)
    emp_dprt = Column(String(100), nullable=False)
    emp_dsgn = Column(String(100), nullable=False)
    date_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    emp_atdnce = Column(String(50), nullable=False)
    leave_reason = Column(String(255), nullable=True) # ✅ New database column
    emp_joindt = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    emp_sal = Column(Float, nullable=False)

    # ✅ Database constraint ensuring only 'present' or 'leave' can be stored
    __table_args__ = (
        CheckConstraint(
            "emp_atdnce IN ('present', 'leave')", 
            name="check_employee_attendance_value"
        ),
    )

    attendance_records = relationship("EmployeeAttendance", back_populates="employee_rel", cascade="all, delete")


class EmployeeAttendance(Base):
    __tablename__ = "employye_attendance"

    emp = Column(Integer, primary_key=True, index=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey("employee_details.emp_id", ondelete="CASCADE"), nullable=False)
    emp_name = Column(String(100), nullable=False)
    emp_atdnce = Column(String(50), nullable=False)
    leave_reason = Column(String(255), nullable=True) # ✅ New database column

    # ✅ Database constraint for attendance logs table
    __table_args__ = (
        CheckConstraint(
            "emp_atdnce IN ('present', 'leave')", 
            name="check_log_attendance_value"
        ),
    )

    employee_rel = relationship("EmployeeDetail", back_populates="attendance_records")


# Automatically generate/update your structural updates in MySQL
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🗺️ FastAPI Route Handlers (API Endpoints)
# ------------------------------------------------------------

@app.get("/")
def home():
    return {"message": "Welcome to the Employee Management API. Go to /docs to test endpoints!"}


# 1. POST /employees (Add employee details)
@app.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    # Automatically clear leave_reason if status is 'present'
    reason = employee.leave_reason if employee.emp_atdnce == "leave" else None
    
    db_employee = EmployeeDetail(
        emp_name=employee.emp_name,
        emp_dprt=employee.emp_dprt,
        emp_dsgn=employee.emp_dsgn,
        emp_atdnce=employee.emp_atdnce,
        leave_reason=reason,
        emp_sal=employee.emp_sal
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return {"message": "Employee details created", "data": db_employee}

# 2. GET /employees (Get all employees)
@app.get("/employees", response_model=List[EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return db.query(EmployeeDetail).all()

# 3. GET /employees/{id} (Get employee by emp_id)
@app.get("/employees/{id}", response_model=EmployeeResponse)
def get_employee_by_id(id: int, db: Session = Depends(get_db)):
    db_employee = db.query(EmployeeDetail).filter(EmployeeDetail.emp_id == id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee details retrieved", "data": db_employee}

# 4. PUT /employees/{id} (Update employee details & attendance reason)
@app.put("/employees/{id}", response_model=EmployeeResponse)
def update_employee(id: int, updated_data: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = db.query(EmployeeDetail).filter(EmployeeDetail.emp_id == id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db_employee.emp_name = updated_data.emp_name
    db_employee.emp_dprt = updated_data.emp_dprt
    db_employee.emp_dsgn = updated_data.emp_dsgn
    db_employee.emp_atdnce = updated_data.emp_atdnce
    db_employee.leave_reason = updated_data.leave_reason if updated_data.emp_atdnce == "leave" else None
    db_employee.emp_sal = updated_data.emp_sal
        
    db.commit()
    db.refresh(db_employee)
    return {"message": "Employee details updated", "data": db_employee}

# 5. DELETE /employees/{id} (Delete employee profile)
@app.delete("/employees/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(id: int, db: Session = Depends(get_db)):
    db_employee = db.query(EmployeeDetail).filter(EmployeeDetail.emp_id == id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return {"message": "Employee deleted"}

# 6. GET /employees/department/{name} (Get employees by department branch)
@app.get("/employees/department/{name}", response_model=List[EmployeeResponse])
def get_employees_by_department(name: str, db: Session = Depends(get_db)):
    return db.query(EmployeeDetail).filter(EmployeeDetail.emp_dprt.ilike(name)).all()

# 7. POST /attendance/{id} (Log attendance check-in record)
# Accepts optional query parameters to dynamically assign 'present'/'leave' and 'leave_reason'
@app.post("/attendance/{id}", response_model=AttendancePostResponseWrapper, status_code=status.HTTP_201_CREATED)
def mark_attendance(
    id: int, 
    status_type: Literal["present", "leave"] = "present", 
    reason: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    db_employee = db.query(EmployeeDetail).filter(EmployeeDetail.emp_id == id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    
    actual_reason = reason if status_type == "leave" else None
    
    # 1. Update the current active status on the master profile
    db_employee.emp_atdnce = status_type
    db_employee.leave_reason = actual_reason
    
    # 2. Append a historical row into your tracking log table
    new_log = EmployeeAttendance(
        emp_id=id,
        emp_name=db_employee.emp_name,
        emp_atdnce=status_type,
        leave_reason=actual_reason
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    
    # Returns the payload matching the AttendancePostResponseWrapper structure
    return {"message": "Attendance marked", "data": new_log}

# 8. GET /attendance (Get all attendance records with formatted output)
@app.get("/attendance", response_class=PlainTextResponse)
def get_attendance_records(db: Session = Depends(get_db)):
    # 1. Fetch all records from the attendance table
    records = db.query(EmployeeAttendance).all()
    
    present_list = []
    leave_list = []
    
    # 2. Loop through records and structure the text lines
    for record in records:
        emp_id = record.emp_id
        emp_name = record.emp_name
        
        # Match your exact lowercase check ("present" or "leave")
        if record.emp_atdnce.lower() == "present":
            present_list.append(f"employee id: {emp_id}\namployee name: {emp_name}")
        else:
            reason = record.leave_reason or "Not Specified"
            leave_list.append(f"employee id: {emp_id}\namployee name: {emp_name}\nreason: {reason}")
            
    # 3. Construct the exact layout you requested
    border = "=" * 50
    
    output = []
    output.append(border)
    output.append(f"{'\"Employees Present\"':>45}")
    # Separates distinct employees by a clean double newline block
    output.append("\n\n".join(present_list) if present_list else "None")
    
    output.append(border)
    output.append(f"{'\"Employees on Leave\"':>46}")
    output.append("\n\n".join(leave_list) if leave_list else "None")
    
    return "\n".join(output)

# 9. GET /high-salary-employees (Get profiles meeting salary threshold)
@app.get("/high-salary-employees", response_model=List[EmployeeResponse])
def get_high_salary_employees(threshold: float = 50000.0, db: Session = Depends(get_db)):
    return db.query(EmployeeDetail).filter(EmployeeDetail.emp_sal >= threshold).all()

# 10. GET /search-employee/{name} (Search employee by name string pattern)
@app.get("/search-employee/{name}", response_model=List[EmployeeResponse])
def search_employee_by_name(name: str, db: Session = Depends(get_db)):
    return db.query(EmployeeDetail).filter(EmployeeDetail.emp_name.ilike(f"%{name}%")).all()
