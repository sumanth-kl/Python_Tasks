# Import required modules to work on FastAPI
from fastapi import FastAPI, HTTPException # Tools to build the web API and send clear error messages to the user
from pydantic import BaseModel # A blueprint that defines exactly what data our application should accept
from typing import List # A way to tell Python we are using a list of specific items (needed for Python 3.8 and older)

app = FastAPI() # Creates the main application object that handles all our API routes

class Todo(BaseModel): # Creating base model using pydantic model
    """Represents a single task in the task management system."""
    id: int # Defining datatypes to accept the values for the application
    title: str
    completed: bool = False

todos = [] # A temporary database (list) to store our tasks while the app is running

@app.post("/todos") # Tells the API to listen for POST requests (sending data) at this URL
def create_todo(todo: Todo): # Receives the data and automatically checks if it matches our Todo model
    todos.append(todo) # Stores the new item in our list of todos
    return {"message": "Todo added", "data": todo} # Sends back a confirmation message and the data we saved

@app.get("/todos") # Tells the API to listen for GET requests (fetching data) at this URL
def get_todos(): # Defining a function to retrieve all your Todo items
    return todos # Sends back the full list of tasks you have stored

@app.get("/todos/{todo_id}") # Listens for GET requests where {todo_id} is a dynamic variable in the URL
def get_todo(todo_id: int): # Takes the ID from the URL and ensures it is an integer
    for todo in todos: # Loops through our list to find a match
        if todo.id == todo_id: # Checks if the current item's ID matches the one we are looking for
            return todo # If found, sends back that specific task
    raise HTTPException(status_code=404, detail="Todo not found") # If the loop finishes without a match, returns an error

@app.put("/todos/{todo_id}") # Listens for PUT requests to update an existing item at a specific ID
def update_todo(todo_id: int, updated_todo: Todo): # Takes the ID from the URL and the new data from the request body
    for index, todo in enumerate(todos): # Loops through the list while keeping track of the position (index)
        if todo.id == todo_id: # Checks if the current item is the one we want to change
            todos[index] = updated_todo # Replaces the old data with the new data at that specific position
            return {"message": "Updated successfully", "data": updated_todo} # Returns a success message and the updated task
    raise HTTPException(status_code=404, detail="Todo not found") # Sends an error if the loop finishes without finding the ID

@app.delete("/todos/{todo_id}") # Listens for DELETE requests to remove a specific item from the list
def delete_todo(todo_id: int): # Receives the ID of the task that needs to be removed
    for index, todo in enumerate(todos): # Loops through the list to find the item and its position
        if todo.id == todo_id: # Checks if the current item matches the ID we want to delete
            deleted = todos.pop(index) # Removes the item from the list and saves it to a variable
            return {"message": "Deleted successfully", "data": deleted} # Confirms the deletion and shows what was removed
    raise HTTPException(status_code=404, detail="Todo not found") # Sends an error if the ID doesn't exist in our list


""" Command to Run this code base.

uvicorn main:app --reload or python -m uvicorn main:app --reload

uvicorn: This is the engine that actually runs the web server.
main: This is the name of your Python file (e.g., main.py). If your file is named todo_api.py, you would type todo_api:app.
:app: This refers to the app = FastAPI() object you created inside that file.
--reload: This is a "magic" flag for developers. It tells the server to automatically restart every time you save your code, so you don't have to stop and start it manually."""