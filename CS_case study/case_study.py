from abc import ABC, abstractmethod
import csv
import json
from functools import wraps

# ================= CUSTOM EXCEPTIONS =================
class DuplicateStudentError(Exception):
    pass


# ================= DECORATORS =================
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get("admin", False):
            raise PermissionError("Access Denied: Admin privileges required")
        return func(*args, **kwargs)
    return wrapper


# ================= ABSTRACT BASE CLASS =================
class Person(ABC):
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass


# ================= DESCRIPTORS =================
class MarksDescriptor:
    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks should be between 0 and 100")
        instance.__dict__["marks"] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get("marks", [])


class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Salary should be positive")
        obj._salary = value


# ================= STUDENT CLASS =================
class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def get_details(self):
        return f"ID: {self.id} | Name: {self.name} | Dept: {self.department} | Semester: {self.semester}"

    @log_execution
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"
        return avg, grade

    def __gt__(self, other):
        return self.calculate_performance()[0] > other.calculate_performance()[0]


# ================= FACULTY CLASS =================
class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        return f"ID: {self.id} | Name: {self.name} | Dept: {self.department}"


# ================= COURSE CLASS =================
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def __add__(self, other):
        return self.credits + other.credits


# ================= ITERATOR =================
class CourseIterator:
    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.courses):
            raise StopIteration
        course = self.courses[self.index]
        self.index += 1
        return course.name


# ================= GENERATORS =================
def marks_generator(marks):
    for m in marks:
        yield m


# ================= FILE HANDLING =================
def save_students_json(students):
    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks,
            "courses": [c.code for c in s.courses]
        })
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Student data saved to students.json")


def save_students_csv(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.id, s.name, s.department, avg, grade])
    print("CSV report generated successfully")


# ================= REGISTRIES =================
students = {}
faculty_members = {}
courses = {}
student_registry = {}


def add_student(student):
    if student.id in student_registry:
        raise DuplicateStudentError("Student ID already exists")
    student_registry[student.id] = student


# ================= MENU FUNCTIONS =================
def add_student_menu():
    try:
        sid = input("Student ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        semester = int(input("Semester: "))
        marks = list(map(int, input("Enter Marks (space separated): ").split()))

        student = Student(sid, name, dept, semester, marks)
        add_student(student)
        students[sid] = student
        print("Student added successfully")

    except Exception as e:
        print("Error:", e)


def add_faculty_menu():
    try:
        fid = input("Faculty ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        salary = float(input("Salary: "))

        faculty = Faculty(fid, name, dept, salary)
        faculty_members[fid] = faculty
        print("Faculty added successfully")

    except Exception as e:
        print("Error:", e)


def add_course_menu():
    try:
        code = input("Course Code: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        fid = input("Faculty ID: ")

        if fid not in faculty_members:
            print("Faculty not found")
            return

        course = Course(code, name, credits, faculty_members[fid])
        courses[code] = course
        print("Course added successfully")

    except Exception as e:
        print("Error:", e)


def enroll_student_menu():
    sid = input("Student ID: ")
    code = input("Course Code: ")

    if sid not in students or code not in courses:
        print("Invalid Student or Course")
        return

    students[sid].enroll(courses[code])
    courses[code].enroll_student(students[sid])
    print("Student enrolled successfully")


def calculate_performance_menu():
    sid = input("Student ID: ")

    if sid not in students:
        print("Student not found")
        return

    avg, grade = students[sid].calculate_performance()
    print(f"Average: {avg:.2f}")
    print(f"Grade  : {grade}")


def compare_students_menu():
    s1 = input("First Student ID: ")
    s2 = input("Second Student ID: ")

    if s1 not in students or s2 not in students:
        print("Invalid Student ID")
        return

    print(f"{students[s1].name} > {students[s2].name} : {students[s1] > students[s2]}")


def generate_reports_menu():
    if not students:
        print("No student data available")
        return
    save_students_json(list(students.values()))
    save_students_csv(list(students.values()))


def exit_system():
    print("Thank you for using Smart University Management System")


# ================= MAIN MENU =================
def main_menu():
    while True:
        print("\nSMART UNIVERSITY MANAGEMENT SYSTEM")
        print("----------------------------------")
        print("1 → Add Student")
        print("2 → Add Faculty")
        print("3 → Add Course")
        print("4 → Enroll Student to Course")
        print("5 → Calculate Student Performance")
        print("6 → Compare Two Students")
        print("7 → Generate Reports")
        print("8 → Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student_menu()
        elif choice == "2":
            add_faculty_menu()
        elif choice == "3":
            add_course_menu()
        elif choice == "4":
            enroll_student_menu()
        elif choice == "5":
            calculate_performance_menu()
        elif choice == "6":
            compare_students_menu()
        elif choice == "7":
            generate_reports_menu()
        elif choice == "8":
            exit_system()
            break
        else:
            print("Invalid choice, try again")


# ================= PROGRAM START =================
if __name__ == "__main__":
    main_menu()
