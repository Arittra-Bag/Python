class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def store(self, marks):
        self.marks.append(marks)

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll}")
        print("Marks in Subjects:")
        for i, mark in enumerate(self.marks, start=1):
            print(f"Subject-{i}: {mark}")

n = int(input("Enter the number of subjects: "))
name = input("Enter student's name: ")
roll = input("Enter student's roll number: ")

stud = Student(name, roll)

for i in range(n):
    marks = int(input(f"Enter Marks for Subject-{i+1}: "))
    stud.store(marks)

stud.display()