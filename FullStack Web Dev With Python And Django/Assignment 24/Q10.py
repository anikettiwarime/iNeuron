# 10. Define a class Employee with instance object variables empid, name, salary.
# Write __init__() method in the class to initialize instance object variables.
# Also define instance methods to input fields and display field values

class Employee:

    def __init__(self):
        self.empid = 0
        self.name = "Emp"
        self.salary = 100000

    def input_Employee_details(self):
        self.empid = input("Enter Employee id : ")
        self.name = input("Enter Employee name : ")
        self.salary = input("Enter Employee salary : ")

    def display(self):
        print(self.empid)
        print(self.name)
        print(self.salary)


e1 = Employee()

e1.input_Employee_details()

e1.display()
