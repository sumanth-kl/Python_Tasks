# ============================================================
# 📝 FastAPI Student Management App (CRUD) - SQLite Database Version
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ------------------------------------------------------------
# 🚀 Create FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ Database Configuration
# ------------------------------------------------------------
DATABASE_URL = "sqlite:///./student.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ------------------------------------------------------------
# 🧱 Database Model (Table)
# ------------------------------------------------------------
class StudentDB(Base):
    __tablename__ = "Student_Details"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    course = Column(String)
    marks = Column(Integer)
    completed = Column(Boolean, default=False)

# Create table
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int
    completed: bool=False

    class Config:
        orm_mode = True

# ------------------------------------------------------------
# 🔌 Dependency (DB Session)
# ------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "FastAPI Student Management with DB 🚀"}

# ------------------------------------------------------------
# ✅ 1. CREATE STUDENT DETAILS
# ------------------------------------------------------------
@app.post("/POST/students")
def create_student(stdnt: Student, db: Session = Depends(get_db)):
    existing = db.query(StudentDB).filter(StudentDB.id == stdnt.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="ID already exists")

    new_student = StudentDB(
        id=stdnt.id,
        name=stdnt.name,
        age=stdnt.age,
        course=stdnt.course,
        marks=stdnt.marks,
        completed=stdnt.completed
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"message": "Student details created", "data": new_student}

# ------------------------------------------------------------
# ✅ 2. READ ALL STUDENTS
# ------------------------------------------------------------
@app.get("/GET/students")
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(StudentDB).all()
    return {"count": len(students), "data": students}

# ------------------------------------------------------------
# ✅ 3. READ SINGLE STUDENT
# ------------------------------------------------------------
@app.get("/GET/students/{stdnt_id}")
def get_individual_student(stdnt_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(StudentDB.id == stdnt_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

# ------------------------------------------------------------
# ✅ 4. UPDATE STUDENT DETAILS
# ------------------------------------------------------------
@app.put("/PUT/students/{stdnt_id}")
def update_individual_student(stdnt_id: int, updated: Student, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(StudentDB.id == stdnt_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name = updated.name
    student.age = updated.age
    student.course = updated.course
    student.marks = updated.marks
    student.completed = updated.completed

    db.commit()
    db.refresh(student)

    return {"message": "Updated successfully", "data": student}

# ------------------------------------------------------------
# ✅ 5. DELETE STUDENT
# ------------------------------------------------------------
@app.delete("/DELETE/students/{stdnt_id}")
def delete_individual_student(stdnt_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(StudentDB.id == stdnt_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student Deleted successfully"}
