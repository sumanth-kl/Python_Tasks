from datetime import datetime, timezone
from typing import List, Literal, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from pymongo import MongoClient

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI(title="Employee Management API (Manual Numeric IDs)")

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection (Pure PyMongo Fixed Setup)
# ------------------------------------------------------------
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["company_db"]

# Define the collections used in your routes
employee_collection = db["employees"]
attendance_collection = db["attendance"]


# ------------------------------------------------------------
# 🧾 Pydantic Schema (Configured for Pydantic V2)
# ------------------------------------------------------------

class EmployeeCreate(BaseModel):
    emp_id: int  # Accept custom integers (1, 2, 3...) manually via request body
    emp_name: str
    emp_dprt: str
    emp_dsgn: str
    emp_atdnce: Literal["present", "leave"]
    leave_reason: Optional[str] = None
    emp_sal: float

class EmployeeResponse(BaseModel):
    emp_id: int  # Primary key tracks your custom integers
    emp_name: str
    emp_dprt: str
    emp_dsgn: str
    date_time: datetime
    emp_atdnce: str
    leave_reason: Optional[str] = None
    emp_joindt: datetime
    emp_sal: float

    model_config = {
        "from_attributes": True
    }

class AttendanceResponse(BaseModel):
    emp: str 
    emp_id: int  # Numeric ID linkage back to employees
    emp_name: str
    emp_atdnce: str
    leave_reason: Optional[str] = None
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }


# ------------------------------------------------------------
# 🗺️ FastAPI Route Handlers (Manual Integer Queries)
# ------------------------------------------------------------

@app.get("/")
def home():
    return {"message": "Welcome to the Direct PyMongo Employee API. Go to /docs to test!"}


# 1. POST /employees (Add employee details with manual integer ID)
@app.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def add_employee(employee: EmployeeCreate):
    # Check if the requested ID already exists inside MongoDB Atlas
    if employee_collection.find_one({"_id": employee.emp_id}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Employee with ID {employee.emp_id} already exists"
        )

    reason = employee.leave_reason if employee.emp_atdnce == "leave" else None
    now_time = datetime.now(timezone.utc)
    
    doc = {
        "_id": employee.emp_id,  # Map custom integer value directly into MongoDB primary key
        "emp_name": employee.emp_name,
        "emp_dprt": employee.emp_dprt,
        "emp_dsgn": employee.emp_dsgn,
        "date_time": now_time,
        "emp_atdnce": employee.emp_atdnce,
        "leave_reason": reason,
        "emp_joindt": now_time,
        "emp_sal": employee.emp_sal
    }
    
    employee_collection.insert_one(doc)
    
    return EmployeeResponse(
        emp_id=doc["_id"],
        emp_name=doc["emp_name"],
        emp_dprt=doc["emp_dprt"],
        emp_dsgn=doc["emp_dsgn"],
        date_time=doc["date_time"],
        emp_atdnce=doc["emp_atdnce"],
        leave_reason=doc["leave_reason"],
        emp_joindt=doc["emp_joindt"],
        emp_sal=doc["emp_sal"]
    )


# 2. GET /employees (Get all employees)
@app.get("/employees", response_model=List[EmployeeResponse])
def get_all_employees():
    raw_employees = list(employee_collection.find())
    return [
        EmployeeResponse(
            emp_id=e["_id"],
            emp_name=e.get("emp_name", ""),
            emp_dprt=e.get("emp_dprt", ""),
            emp_dsgn=e.get("emp_dsgn", ""),
            date_time=e.get("date_time", datetime.now(timezone.utc)),
            emp_atdnce=e.get("emp_atdnce", "present"),
            leave_reason=e.get("leave_reason"),
            emp_joindt=e.get("emp_joindt", datetime.now(timezone.utc)),
            emp_sal=e.get("emp_sal", 0.0)
        ) for e in raw_employees
    ]


# 3. GET /employees/{id} (Get employee by integer ID)
@app.get("/employees/{id}", response_model=EmployeeResponse)
def get_employee_by_id(id: int):
    e = employee_collection.find_one({"_id": id})
    if not e:
        raise HTTPException(status_code=404, detail="Employee not found")
        
    return EmployeeResponse(
        emp_id=e["_id"], 
        emp_name=e.get("emp_name", ""), 
        emp_dprt=e.get("emp_dprt", ""), 
        emp_dsgn=e.get("emp_dsgn", ""),
        date_time=e.get("date_time", datetime.now(timezone.utc)), 
        emp_atdnce=e.get("emp_atdnce", "present"), 
        leave_reason=e.get("leave_reason"), 
        emp_joindt=e.get("emp_joindt", datetime.now(timezone.utc)), 
        emp_sal=e.get("emp_sal", 0.0)
    )


# 4. PUT /employees/{id} (Update employee details)
@app.put("/employees/{id}", response_model=EmployeeResponse)
def update_employee(id: int, updated_data: EmployeeCreate):
    e = employee_collection.find_one({"_id": id})
    if not e:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    reason = updated_data.leave_reason if updated_data.emp_atdnce == "leave" else None
    
    employee_collection.update_one(
        {"_id": id},
        {"$set": {
            "emp_name": updated_data.emp_name,
            "emp_dprt": updated_data.emp_dprt,
            "emp_dsgn": updated_data.emp_dsgn,
            "emp_atdnce": updated_data.emp_atdnce,
            "leave_reason": reason,
            "emp_sal": updated_data.emp_sal
        }}
    )
    
    updated_doc = employee_collection.find_one({"_id": id})
    return EmployeeResponse(
        emp_id=updated_doc["_id"], 
        emp_name=updated_doc.get("emp_name", ""), 
        emp_dprt=updated_doc.get("emp_dprt", ""),
        emp_dsgn=updated_doc.get("emp_dsgn", ""), 
        date_time=updated_doc.get("date_time", datetime.now(timezone.utc)), 
        emp_atdnce=updated_doc.get("emp_atdnce", "present"), 
        leave_reason=updated_doc.get("leave_reason"), 
        emp_joindt=updated_doc.get("emp_joindt", datetime.now(timezone.utc)), 
        emp_sal=updated_doc.get("emp_sal", 0.0)
    )


# 5. DELETE /employees/{id} (Delete employee profile)
@app.delete("/employees/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(id: int):
    result = employee_collection.delete_one({"_id": id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    attendance_collection.delete_many({"emp_id": id})
    return None


# 6. GET /employees/department/{name} (Get employees by department)
@app.get("/employees/department/{name}", response_model=List[EmployeeResponse])
def get_employees_by_department(name: str):
    employees = list(employee_collection.find({"emp_dprt": {"$regex": f"^{name}$", "$options": "i"}}))
    return [
        EmployeeResponse(
            emp_id=e["_id"], 
            emp_name=e.get("emp_name", ""), 
            emp_dprt=e.get("emp_dprt", ""), 
            emp_dsgn=e.get("emp_dsgn", ""),
            date_time=e.get("date_time", datetime.now(timezone.utc)), 
            emp_atdnce=e.get("emp_atdnce", "present"), 
            leave_reason=e.get("leave_reason"), 
            emp_joindt=e.get("emp_joindt", datetime.now(timezone.utc)), 
            emp_sal=e.get("emp_sal", 0.0)
        ) for e in employees
    ]


# 7. POST /attendance/{id} (Log attendance check-in record)
@app.post("/attendance/{id}", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
def mark_attendance(
    id: int, 
    status_type: Literal["present", "leave"] = "present", 
    reason: Optional[str] = None
):
    e = employee_collection.find_one({"_id": id})
    if not e:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    
    actual_reason = reason if status_type == "leave" else None
    now_time = datetime.now(timezone.utc)
    
    employee_collection.update_one(
        {"_id": id},
        {"$set": {"emp_atdnce": status_type, "leave_reason": actual_reason}}
    )
    
    log_doc = {
        "emp_id": id,
        "emp_name": e.get("emp_name", "Unknown"),
        "emp_atdnce": status_type,
        "leave_reason": actual_reason,
        "timestamp": now_time
    }
    result = attendance_collection.insert_one(log_doc)
    
    return AttendanceResponse(
        emp=str(result.inserted_id),
        emp_id=log_doc["emp_id"],
        emp_name=log_doc["emp_name"],
        emp_atdnce=log_doc["emp_atdnce"],
        leave_reason=log_doc["leave_reason"],
        timestamp=log_doc["timestamp"]
    )


# 8. GET /attendance (Get historical attendance logs)
@app.get("/attendance", response_model=List[AttendanceResponse])
def get_attendance_records():
    logs = list(attendance_collection.find())
    return [
        AttendanceResponse(
            emp=str(l["_id"]), 
            emp_id=l.get("emp_id", 0), 
            emp_name=l.get("emp_name", "Unknown"),
            emp_atdnce=l.get("emp_atdnce", "present"), 
            leave_reason=l.get("leave_reason"), 
            timestamp=l.get("timestamp", datetime.now(timezone.utc))
        ) for l in logs
    ]


# 9. GET /high-salary-employees (Get profiles meeting salary threshold)
@app.get("/high-salary-employees", response_model=List[EmployeeResponse])
def get_high_salary_employees(threshold: float = 50000.0):
    employees = list(employee_collection.find({"emp_sal": {"$gte": threshold}}))
    return [
        EmployeeResponse(
            emp_id=e["_id"], 
            emp_name=e.get("emp_name", ""), 
            emp_dprt=e.get("emp_dprt", ""), 
            emp_dsgn=e.get("emp_dsgn", ""),
            date_time=e.get("date_time", datetime.now(timezone.utc)), 
            emp_atdnce=e.get("emp_atdnce", "present"), 
            leave_reason=e.get("leave_reason"), 
            emp_joindt=e.get("emp_joindt", datetime.now(timezone.utc)), 
            emp_sal=e.get("emp_sal", 0.0)
        ) for e in employees
    ]


# 10. GET /search-employee/{name} (Search employee by name string pattern)
@app.get("/search-employee/{name}", response_model=List[EmployeeResponse])
def search_employee_by_name(name: str):
    employees = list(employee_collection.find({"emp_name": {"$regex": name, "$options": "i"}}))
    return [
        EmployeeResponse(
            emp_id=e["_id"], 
            emp_name=e.get("emp_name", ""), 
            emp_dprt=e.get("emp_dprt", ""), 
            emp_dsgn=e.get("emp_dsgn", ""),
            date_time=e.get("date_time", datetime.now(timezone.utc)), 
            emp_atdnce=e.get("emp_atdnce", "present"), 
            leave_reason=e.get("leave_reason"), 
            emp_joindt=e.get("emp_joindt", datetime.now(timezone.utc)), 
            emp_sal=e.get("emp_sal", 0.0)
        ) for e in employees
    ]
