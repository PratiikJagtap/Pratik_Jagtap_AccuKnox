from fastapi import FastAPI

app = FastAPI()

STUDENTS_DATA = [
    {"name": "Aarav",   "score": 85},
    {"name": "Rohan",   "score": 78},
    {"name": "Siddharth", "score": 94},
    {"name": "Priya",   "score": 88},
    {"name": "pratik",   "score": 86},
    {"name": "raju",   "score": 77},
    {"name": "vivek", "score": 92},
    {"name": "rani",   "score": 81},
    {"name": "rohit",   "score": 82},
    {"name": "akash",   "score": 75},
    {"name": "juhi", "score": 90},
    {"name": "siddhi",   "score": 84},

]

@app.get("/students")
def get_students():
    return STUDENTS_DATA
