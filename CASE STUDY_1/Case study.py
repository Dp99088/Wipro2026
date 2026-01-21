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


# ================= DEPARTMENT CLASS =================
class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.faculty = []

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)


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
        return f"Name      : {self.name}\nRole      : Student\nDepartment: {self.department}"

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
        return f"Name      : {self.name}\nRole      : Faculty\nDepartment: {self.department}"


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
def student_generator(students):
    print("Fetching Student Records...")
    for s in students:
        yield f"{s.id} - {s.name}"


def marks_generator(marks):
    for m in marks:
        yield m


# ================= STUDENT PERFORMANCE REPORT =================
def student_performance_report(student):
    print("\nStudent Performance Report")
    print("--------------------------------")
    total = sum(marks_generator(student.marks))
    average = total / len(student.marks)
    grade = "A" if average >= 80 else "B" if average >= 60 else "C"
    print(f"Student Name : {student.name}")
    print(f"Marks        : {student.marks}")
    print(f"Average      : {average:.1f}")
    print(f"Grade        : {grade}")
    print("(Average calculated using generator / iterator)")


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
    print("Student data successfully saved to students.json")


def save_students_csv(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.id, s.name, s.department, avg, grade])
    print("CSV Report Generated Successfully")


def load_students_json(filename):
    try:
        with open(filename, "r") as f:
            json.load(f)
            print("Student data loaded successfully")
    except FileNotFoundError:
        print("Error: File not found")


# ================= REGISTRY & EXCEPTION HANDLING =================
student_registry = {}

def add_student(student):
    if student.id in student_registry:
        raise DuplicateStudentError("Error: Student ID already exists")
    student_registry[student.id] = student
    print("Student Created Successfully")


# ================= ADMIN DECORATOR DEMO =================
@admin_only
def admin_task():
    print("Admin task executed")


# ================= EXIT FUNCTION =================
def exit_system():
    print("Thank you for using Smart University Management System")


# ================= SAMPLE EXECUTION =================
s1 = Student("S101", "Ananya Sharma", "Computer Science", 4, [78, 85, 90, 88, 92])
s2 = Student("S102", "Rohan Verma", "Computer Science", 4, [70, 72, 75, 78, 74])

f1 = Faculty("F201", "Dr. Rajesh Kumar", "Computer Science", 85000)

c1 = Course("CS401", "Data Structures", 4, f1)
c2 = Course("CS402", "Algorithms", 3, f1)

s1.enroll(c1)
c1.enroll_student(s1)

# ----------------- DETAILS -----------------
print("\nStudent Details\n----------------------------")
print(s1.get_details())

print("\nFaculty Details\n----------------------------")
print(f1.get_details())

# ----------------- STUDENT PERFORMANCE REPORT -----------------
student_performance_report(s1)

# ----------------- COMPARISON -----------------
print("\nComparing Students Performance")
print("Ananya Sharma > Rohan Verma :", s1 > s2)

# ----------------- COURSE CREDITS -----------------
print("\nMerge Course Credits")
print("Total Credits After Merge :", c1 + c2)

# ----------------- GENERATOR -----------------
print("\nStudent Record Generator\n----------------------------")
for rec in student_generator([s1, s2]):
    print(rec)

# ----------------- ITERATOR -----------------
print("\nCourse Iterator\n----------------------------")
for course in CourseIterator([c1, c2]):
    print(course)

# ----------------- FILE OUTPUT -----------------
save_students_json([s1, s2])
save_students_csv([s1, s2])

# ----------------- DESCRIPTOR VALIDATION -----------------
print("\nDescriptor Validation Output\n----------------------------")
try:
    Student("S103", "Invalid Student", "CS", 3, [90, 110, 85])
except ValueError as e:
    print("Invalid Marks")
    print(f"Error: {e}")

try:
    print(f1.salary)
except PermissionError as e:
    print("Unauthorized Salary Access")
    print(e)

# ----------------- DECORATOR OUTPUT -----------------
print("\nDecorator Output\n----------------------------")
s1.calculate_performance()

try:
    admin_task()
except PermissionError as e:
    print(e)

# ----------------- EXCEPTION HANDLING -----------------
try:
    add_student(s1)
    add_student(s1)
except DuplicateStudentError as e:
    print(e)

load_students_json("missing_file.json")

# ----------------- EXIT -----------------
exit_system()
