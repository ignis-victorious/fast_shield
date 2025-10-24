#
#  Import LIBRARIES
import uvicorn
from fastapi import FastAPI

from routers import general_router, students_router, subjects_router

# from db.students_db import students_db

# from pydantic import BaseModel
#  Import FILES
# from models.student import Student

# from routers import student_router

#

"""
📂 models/      - Data structures (what our data looks like)
📂 database/    - Database logic (where our data is stored)
📂 routers/     - API routes (different pages/endpoints)
📄 main.py      - This file brings everything together
"""


app: FastAPI = FastAPI(
    title="Student API - Beginner Tutorial", description="A simple API for managing students", version="1.0.1"
)


# WE WILL PLACE OUR ROUTERS HERE
app.include_router(router=general_router)
app.include_router(router=students_router)
app.include_router(router=subjects_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)

#
#  Import LIBRARIES
#  Import FILES
#


# @app.get(path="/")
# def home() -> dict[str, str | dict[str, str]]:
#     """
#     HOME ROUTE:
#     The home page for our API
#     Visit http://localhost:8000 to get here
#     """
#     return {
#         "message": "Welcome to the Student API! 💡",
#         "tip": "Go to /docs to see all endpoints",
#         "endpoints": {
#             "Get all students": "/students",
#             "Get one student": "/students/{id}",
#             "Add a student": "/students (POST)",
#             "Update a student": "/students/{id} (PUT)",
#             "Delete a student": "/students/{id} (DELETE)",
#         },
#     }


# @app.get(
#     path="/students",
# )
# def get_all_students() -> dict[str, int | list[dict[str, int | str]]]:
#     """
#     Get all students from the database
#     This is a GET request - it just retieves data for the students
#     """
#     return {"total_students": len(students_db), "students": students_db}


# @app.get(path="/students/{student_id}")
# def get_one_student(student_id: int) -> dict[str, int | str] | None:
#     """
#     Get one specific student by their ID.
#     The {student_id} comes from the URL path.
#     Example: /students/1 will get the student with ID 1
#     """

#     # Look for the student with the matching ID
#     for student in students_db:
#         if student["id"] == student_id:
#             return student
#             # If not found, return an error message
#             return {"error": f"Student with ID {student_id} not found"}


# @app.post(path="/students")
# def add_student(student: Student):
#     """
#     Add a new student to our database.
#     This is a POST request - it adds new data.
#     The student data comes from the request body as JSON.
#     FastAPI automatically validates it using our Student model!
#     """
#     # Create a new student with an auto-generated ID - {"name": "Elle", "age": 110, "grade": "n/a"}
#     new_student: dict[str, int | str] = {
#         "id": len(students_db) + 1,
#         # Simple ID generation
#         "name": student.name,
#         "age": student.age,
#         "grade": student.grade,
#     }

#     # Add to our "database"
#     students_db.append(new_student)

#     return {"message": f"Student {student.name} added successfully!", "student": new_student}


# @app.put(path="/stjudents/(student_id)")
# def update_student(student_id: int, student: Student) -> dict[str, str | dict[str, int | str]] | None:
#     """
#     Update an existing student's information.
#     This is a PUT request - it modifies existing data.
#     You need to provide:
#     1. The student ID in the URL (which student to update)
#     2. The new student data in the request body (what to change)
#     """
#     # Find the student with the matching ID
#     for i, existing_student in enumerate(students_db):
#         if existing_student["id"] == student_id:
#             # Update the student's information
#             students_db[i] = {
#                 "id": student_id,
#                 # Keep the same ID
#                 "name": student.name,
#                 "age": student.age,
#                 "grade": student.grade,
#             }
#             return {"message": f"Student {student.name} updated successfully!", "student": students_db[i]}
#     # If student not found
#     return {"error": f"Student with ID {student_id} not found"}


# # DELETE A STUDENT
# @app.delete(path="/students/(student_id) ")
# def delete_student(student_id: int) -> dict[str, str | dict[str, int | str]] | dict[str, str]:
#     """
#     Delete a student from our database.
#     This is a DELETE request - it removes data.
#     You only need to provide the student ID in the URL.
#     """

#     # Find and remove the student with the matching ID
#     for i, student in enumerate(iterable=students_db):
#         if student["id"] == student_id:
#             deleted_student: dict[str, int | str] = students_db.pop(i)  # Remove from list
#             return {
#                 "message": f"Student {deleted_student['name']} deleted successfully!",
#                 "deleted_student": deleted_student,
#             }
#     # If student not found
#     return {"error": f"Student with ID {student_id} not found"}
