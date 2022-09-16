# 9. Write a python program to create a function to check whether a number falls in a given range.

def check_range(a, b, value):

    r = range(a, b+1)

    if value in r:
        print(value, 'is in given range')
    else:
        print(value, 'is not in given range')


check_range(5, 50, 51)
check_range(5, 50, 11)
