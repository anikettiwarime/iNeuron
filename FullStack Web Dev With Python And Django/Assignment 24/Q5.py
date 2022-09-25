# 5. Write a python program to delete the age property of the user.
class User:
    def __init__(self):
        self.age = 10
        self.name = "Aniket"


U1 = User()

print(U1.age)
print(U1.name)

del U1.age

print(U1.age) # This will give an error as age is deleted
print(U1.name)
