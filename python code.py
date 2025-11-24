class Student:
    def __init__(self, name, roll_number, age, grade):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grade = grade

    def display_student(self):
        print(f"Name: {self.name}, Roll No: {self.roll_number}, Age: {self.age}, Grade: {self.grade}")

def add_student(students_list):
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    student = Student(name, roll_number, age, grade)
    students_list.append(student)
    print("Student added successfully!")

def display_all_students(students_list):
    if not students_list:
        print("No students in the system.")
        return
    print("\n--- All Students ---")
    for student in students_list:
        student.display_student()
    print("--------------------")

def search_student(students_list):
    roll_number = input("Enter roll number to search: ")
    found = False
    for student in students_list:
        if student.roll_number == roll_number:
            print("\n--- Student Found ---")
            student.display_student()
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student(students_list):
    roll_number = input("Enter roll number to delete: ")
    initial_len = len(students_list)
    students_list[:] = [student for student in students_list if student.roll_number != roll_number]
    if len(students_list) < initial_len:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def main():
    students = []
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
