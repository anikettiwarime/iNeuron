# 5. Write a python program to create a function to find the Min of three numbers.

def min_of_3(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    elif b < c:
        return b
    else:
        return c


print(min(4, 3, 1))
