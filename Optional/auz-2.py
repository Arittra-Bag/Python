class BasicInformation:
    def __init__(self, name, empid, age):
        self.name = name
        self.empid = empid
        self.age = age

class DepartmentInformation:
    def __init__(self, dept_name, assigned_work, time_to_complete):
        self.dept_name = dept_name
        self.assigned_work = assigned_work
        self.time_to_complete = time_to_complete

class Employee(BasicInformation, DepartmentInformation):
    def __init__(self, name, empid, age, dept_name, assigned_work, time_to_complete):
        BasicInformation.__init__(self, name, empid, age)
        DepartmentInformation.__init__(self, dept_name, assigned_work, time_to_complete)

    def display_info(self):
        print("\nEmployee Name:", self.name)
        print("Employee ID:", self.empid)
        print("Age:", self.age)
        print("Department Name:", self.dept_name)
        print("Assigned Work:", self.assigned_work)
        print("Time to Complete Work:", self.time_to_complete)

employees = []
num_employees = int(input("Enter the number of employees: "))

for i in range(num_employees):
    print(f"Enter details for Employee-{i + 1}:")
    name = input("Name: ")
    empid = int(input("Employee ID: "))
    age = int(input("Age: "))
    dept_name = input("Department Name: ")
    assigned_work = input("Assigned Work: ")
    time_to_complete = input("Time to Complete Work: ")

    employee = Employee(name, empid, age, dept_name, assigned_work, time_to_complete)
    employees.append(employee)

for i, employee in enumerate(employees, start=1):
    print(f"Employee {i} Details:")
    employee.display_info()