# 7. Write a python program to access a function inside a function.

def fun1():
    print('Function 1 running')

    for i in range(10):
        print(end='*')
    print()
    print('Function 1 stoped')


def fun2():
    print('Function 2 running')
    fun1()
    print('Function 2 stoped')


fun2()
