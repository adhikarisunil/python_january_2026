import os



class Student:
    def __init__(self, name, roll, age, grade):
        self.name = name
        self.roll = roll
        self.age = age
        self.grade = grade

    def to_dict(self):
        return{
            "name": self.name,
            "roll": self.roll,
            "age": self.age,
            "grade": self.grade
        }
    
#File Handling

FILE_NAME = "students.txt"

#Save student in file
def save_student(student):
    with open(FILE_NAME, "a") as f:
        f.write(f"{student.name}, {student.roll}, {student.age}, {student.grade}\n")



#Load Students
def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                  name, roll, age , grade = line.split(",")
                  students.append(Student(name, roll, age, grade))
    return students              

#ave all students
def save_all_students(students):
    with open(FILE_NAME, "w") as f:
        for student in students:
            f.write(f"{student.name},{student.roll},{student.age},{student.grade}")

#Add Student
def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll: ")
    age = input("Enter age: ")
    grade = input("Enter grade")

    student = Student(name, roll, age ,grade)
    save_student(student)


#View Students

def view_students():
    students = load_students()
    if not students:
        print("Student not found.")
        return
    print(f"{'Name':15} {'Roll':10} {'Age':5} {'Grade':5}")
    print("-"*40)

    for student in students:
        print(f"{student.name:15}{student.roll:15}{student.age:15}{student.grade:15}")
    print(f"Total number of students is {len(students)}.")




def search_students():
    query = input("Enter name or roll to search: ").lower()
    students = load_students()
    found = False

    for student in students:
        if query in student.name.lower() or query ==student.roll:
            print(f"Found: Name:{student.name}, Roll: {student.roll}, Age: {student.age}, Grade: {student.grade}")
            found = True

    if not found:
        print(("Student not found."))


def update_student():
    roll = input("Enter roll number to update: ")
    students = load_students()

    for student in students:
        if student.roll == roll:
            print(f"Current info: Name:{student.name}, Age: {student.age}, Grade: {student.grade}")
            student.name = input("Enter new name: ") or student.name
            student.age = input("Enter new age: ") or student.age
            student.grade = input("Enter new grade: ") or student.grade

            save_all_students(students)
            print("Successfully updated")
            return
        
    print("Student not found.")



#Delete student

def delete_student():
    roll = input("Enter roll number to delete: ")
    students = load_students()
    for index, student in enumerate(students):
        if student.roll == roll:
            students.pop(index)
            save_all_students(students)
            print("Successfully deleted.")
            return
    print("Student not found.")





#Main Function
def menu():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_students()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")


#Run program

if __name__=="__main__":
    menu()