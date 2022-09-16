# 6. Write a python program to create a function and print a list where the values are
# square of numbers between 1 and 30.


def list_of_30_square():
    l = []
    for i in range(1, 30+1):
        l.append(i**2)
    print()
    print(l)


list_of_30_square()
