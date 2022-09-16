# 3. Write a python program to create a function which expects an unknown number of arguments.

def fun(*n):
    for i in n:
        print(i)


fun(10, 20, 30, 45)
