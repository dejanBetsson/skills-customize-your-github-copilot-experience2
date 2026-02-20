from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# TODO: Define the Student model using Pydantic
# Fields: id (int), name (str), grade (str)
class Student(BaseModel):
    pass


# In-memory storage for students
students = []


# TODO: Implement GET / — return a welcome message
@app.get("/")
def root():
    pass


# TODO: Implement GET /students — return all students
@app.get("/students")
def get_students():
    pass


# TODO: Implement POST /students — add a new student
@app.post("/students")
def add_student(student: Student):
    pass


# TODO: Implement GET /students/{id} — return a student by ID
# Raise HTTPException with status_code=404 if not found
@app.get("/students/{student_id}")
def get_student(student_id: int):
    pass


# TODO: Implement DELETE /students/{id} — remove a student by ID
# Raise HTTPException with status_code=404 if not found
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    pass
