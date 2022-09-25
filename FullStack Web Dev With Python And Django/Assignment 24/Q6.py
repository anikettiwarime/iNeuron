# 6. Write a python program to create 3 user objects and find the youngest of all.
from tkinter import N


class User:
    def __init__(self):
        self.age = 0
        self.name = ''


user1 = User()
user2 = User()
user3 = User()

user1.age = 10
user1.name = "U1"

user2.age = 15
user2.name = "U2"

user3.age = 5
user3.name = "U3"

if (user1.age < user2.age):
    if user1.age < user3.age:
        print(user1.name)
    else:
        print(user3.name)
else:
    if user2.age < user3.age:
        print(user2.name)
    else:
        print(user3.name)
