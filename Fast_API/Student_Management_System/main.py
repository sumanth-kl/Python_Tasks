from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int
    completed: bool=False

std = []

@app.post("/POST/students")
def create_student(stdnt: Student):
    std.append(stdnt)
    return {"message": "Student added succesfully", "data": stdnt}

@app.get("/GET/students")
def get_all_students():
    return std

@app.get("/GET/students/{stdnt_id}")
def get_individual_student(stdnt_id: int):
    for s in std:
        if s.id == stdnt_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/PUT/students/{stdnt_id}")
def update_individual_student_details(stdnt_id: int, updated_student: Student):
    for i, s in enumerate(std):
        if s.id == stdnt_id:
            std[i] =  updated_student
            return {"message": "Updated successfully", "data": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/DELETE/students/{stdnt_id}")
def delete_individual_student(stdnt_id: int):
    for i, s in enumerate(std):
        if s.id == stdnt_id:
            deleted = std.pop(i)
            return {"message": "Student deleted successfully", "data": deleted} 
    raise HTTPException(status_code=404, detail="Student not found")