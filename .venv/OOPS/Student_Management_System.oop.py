class Student:
    def __init__(self, name, age, roll_number):  # Corrected the constructor name
        self.name = name
        self.age = age
        self.roll_number = roll_number


class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, roll_number):
        student = Student(name, age, roll_number)
        self.students.append(student)

    def display_students(self):  # Corrected the method name
        for student in self.students:  # Corrected the variable name
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Roll No: {student.roll_number}")
            print(" ------------------------------------------- ")

    def edit_student(self,roll_number,new_name,new_age):
        for student in self.students:
            if student.roll_number==roll_number:
                student.name=new_name
                student.age=new_age
                print(f"Student {student.name} Successfully Updates")
                return
    def delete_student(self,roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student {student.name} delete successfully")



school = School()

while True:
    choice=input("Enter your Choices: \n1)Add student \n2)Display list of student \n3)Edit Student Details \n4)Delete Student Details \n5)quitv \n")
    if choice=="1":
        name = input("Enter name of student: ")
        age = input("Enter age: ")
        roll_number = input("Enter roll number: ")

        school.add_student(name, age, roll_number)
    elif choice=="2":
        school.display_students()
    elif choice=="3":
        roll_number= input("Enter roll no which you want to edit")
        new_name=input("Enter new name for studnet")
        new_age=input("Enter new Age for studnet")
        school.edit_student(roll_number,new_name, new_age)
    elif choice=="4":
        roll_number=input("Enter Roll No U want to delete")
        school.display_students(roll_number)
    elif choice=="quit":
        break






school.display_students()  # Corrected the method call
