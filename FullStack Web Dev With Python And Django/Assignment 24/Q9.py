# 9. Write a python program to create a School class and 3 instance variables and 1 class variable.

class School:
    schoolName = "GCEK"

    def __init__(self):
        self.classrooms = 10
        self.schoolType = "Primary"
        self.students = 700


s1 = School()
print(School.schoolName)  # Class Variable
print(s1.classrooms)  # instance Variable
print(s1.schoolType)  # instance Variable
print(s1.students)  # instance Variable
