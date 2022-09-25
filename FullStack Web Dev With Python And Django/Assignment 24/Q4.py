# 4. Write a python program to init default values for user object using __init__ method.
class User:
    def __init__(self):
        self.x = 10


u1 = User()
u2 = User()


print(u1.x)
print(u2.x)
