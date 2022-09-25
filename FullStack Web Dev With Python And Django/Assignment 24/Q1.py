# 1. Write a python program to create a user class with 3 properties: name, age, email.

class User:
    name = ''
    age = ''
    email = ''

    def show(self):
        print("User Details")
        print(self.name)
        print(self.age)
        print(self.email)


A = User()

A.age = 16
A.name = "Aniket"
A.email = 'aniket@email.com'

A.show()