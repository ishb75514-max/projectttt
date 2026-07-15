import json
import os

FILE_NAME = "byishika/students.json"


# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# # Calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"


# # Add student
def add_student(data):
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    math = int(input("Math Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))

    total = math + science + english
    average = total / 3
    grade = calculate_grade(average)

    student = {
        "Roll": roll,
        "Name": name,
        "Math": math,
        "Science": science,
        "English": english,
        "Total": total,
        "Average": round(average, 2),
        "Grade": grade
    }

    data.append(student)
    save_data(data)
    print("\nStudent Added Successfully!\n")


# # Display students
def display_students(data):
    if not data:
        print("No records found.")
        return

    print("\n------ Student Records ------")
    for s in data:
        print(f"""
Roll    : {s['Roll']}
Name    : {s['Name']}
Math    : {s['Math']}
Science : {s['Science']}
English : {s['English']}
Total   : {s['Total']}
Average : {s['Average']}
Grade   : {s['Grade']}
-----------------------------
""")


# Search student
def search_student(data):
    roll = input("Enter Roll Number: ")

    for s in data:
        if s["Roll"] == roll:
            print("\nStudent Found")
            print(s)
            return

    print("Student Not Found.")


# # Class statistics
def statistics(data):
    if not data:
        print("No data available.")
        return

    topper = max(data, key=lambda x: x["Total"])
    avg_class = sum(s["Average"] for s in data) / len(data)

    print("\n------ Class Statistics ------")
    print("Total Students :", len(data))
    print("Class Average  :", round(avg_class, 2))
    print("Topper         :", topper["Name"])
    print("Highest Marks  :", topper["Total"])


# # Main Menu
students = load_data()

while True:
    print("""
========= Student Performance Analyzer =========
1. Add Student
2. Display Students
3. Search Student
4. Class Statistics
5. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        display_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        statistics(students)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")