import json

class Student_class:
    def __init__(self, name, roll_no, age, course):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course
    def display_method(self):
        print("*"*30)
        print("Name: ",self.name)
        print("Roll no: ",self.roll_no)
        print("Age: ",self.age)
        print("Course: ",self.course)
    def to_dict(self):
        return {
            "name":self.name,
            "roll_no": self.roll_no,
            "age": self.age,
            "course": self.course
        }

def get_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid, Enter a integer.")

def add_student():
    name = input("Enter name: ")
    roll_no = get_integer("Enter Roll no: ")
    age = get_integer("Enter age: ")
    course = input("Enter Course: ")
    if roll_no in students:
        print("Student already exists.")
    else:
        student = Student_class(name,roll_no,age,course)
        students[student.roll_no] = student

def display_student():
    roll = get_integer("Enter roll no: ")
    student_object=students.get(roll)
    if student_object is None:
        print("Student not found.")      
    else:
        student_object.display_method()

def update_student():
    roll = get_integer("Enter Roll no: ")
    student_object=students.get(roll)
    if student_object is None:
        print("No such student found.")
    else:
        name = input("Enter new name: ")
        age = get_integer("Enter new age: ")
        course = input("Enter new course name: ")
        student_object.name = name
        student_object.age = age
        student_object.course = course

def delete_student():
    roll = get_integer("Enter student roll no to delete: ")
    if roll in students:
        students.pop(roll)
        print("Student data deleted.")
    else:
        print("Student not found.")

def save_students():
    dic = {}
    for i, j in students.items():
        dic[i]=j.to_dict()
    with open("studentdb", "w") as file:
        json.dump(dic, file, indent=4)

def load_students():
    with open("studentdb", "r") as file:
        dic=json.load(file)
    students={}
    for i,j in dic.items():
        students[int(i)]=Student_class(j["name"],j["roll_no"],j["age"],j["course"])
    return students

def display_all():
    if not students:
        print("No students found.")
        return

    for student in students.values():
        student.display_method()
        print("-" * 30)

try:
    students=load_students()
except (FileNotFoundError, json.JSONDecodeError):
    with open("studentdb", "w") as file:
        json.dump({},file)
    students={}

while True:
    task = get_integer("============Menu============\n"
                       "Add student(1)\n"
                       "Display Student(2)\n"
                       "Update Student(3)\n"
                       "Delete Student(4)\n"
                       "Show complete Data(5)\n"
                       "Exit(6)\n"
                       "Choose: ")
    if task==1:
        add_student()
        save_students()
    elif task==2:
        display_student()
    elif task==3:
        update_student()
        save_students()
    elif task==4:
        delete_student()
        save_students()
    elif task==5:
        display_all()
    elif task==6:
        print("Get Lost")
        save_students()
        break
    else:
        print("Enter valid input...")

