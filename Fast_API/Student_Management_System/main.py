# Import required modules to work on FastAPI
from fastapi import FastAPI, HTTPException # Tools to build the web API and send clear error messages to the user
from pydantic import BaseModel # A blueprint that defines exactly what data our application should accept

app=FastAPI() # Creates the main application object that handles all our API routes

class Student(BaseModel): # Creating base model using pydantic model
    """Represents a single task in the task management system."""
    id: int # Defining datatypes to accept the values for the application
    name: str
    age: int
    course: str
    marks: int
    completed: bool=False

std = [] # A temporary database (list) to store our tasks while the app is running

@app.post("/POST/students") # Tells the API to listen for POST requests (sending data) at this URL
def create_student(stdnt: Student): # Receives the data and automatically checks if it matches our Todo model
    std.append(stdnt) # Stores the new item in our list of todos
    return {"message": "Student added succesfully", "data": stdnt} # Sends back a confirmation message and the data we saved

@app.get("/GET/students")  # Tells the API to listen for GET requests (fetching data) at this URL
def get_all_students(): # Defining a function to retrieve all your Todo items
    return std # Sends back the full list of tasks you have stored

@app.get("/GET/students/{stdnt_id}") # Listens for GET requests where {todo_id} is a dynamic variable in the URL
def get_individual_student(stdnt_id: int):  # Takes the ID from the URL and ensures it is an integer
    for s in std: # Loops through our list to find a match
        if s.id == stdnt_id: # Checks if the current item's ID matches the one we are looking for
            return s # If found, sends back that specific task
    raise HTTPException(status_code=404, detail="Student not found") # If the loop finishes without a match, returns an error

@app.put("/PUT/students/{stdnt_id}") # Listens for PUT requests to update an existing item at a specific ID
def update_individual_student_details(stdnt_id: int, updated_student: Student):  # Takes the ID from the URL and the new data from the request body
    for i, s in enumerate(std): # Loops through the list while keeping track of the position (index)
        if s.id == stdnt_id: # Checks if the current item is the one we want to change
            std[i] =  updated_student # Replaces the old data with the new data at that specific position
            return {"message": "Updated successfully", "data": updated_student} # Returns a success message and the updated task
    raise HTTPException(status_code=404, detail="Student not found") # Sends an error if the loop finishes without finding the ID

@app.delete("/DELETE/students/{stdnt_id}") # Listens for DELETE requests to remove a specific item from the list
def delete_individual_student(stdnt_id: int): # Receives the ID of the task that needs to be removed
    for i, s in enumerate(std): # Loops through the list to find the item and its position
        if s.id == stdnt_id: # Checks if the current item matches the ID we want to delete
            deleted = std.pop(i) # Removes the item from the list and saves it to a variable
            return {"message": "Student deleted successfully", "data": deleted} # Confirms the deletion and shows what was removed
    raise HTTPException(status_code=404, detail="Student not found") # Sends an error if the ID doesn't exist in our list