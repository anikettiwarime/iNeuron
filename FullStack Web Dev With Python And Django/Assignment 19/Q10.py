# 10. Write a python program to create a function to check whether a given number is even or odd.

def even_odd(x):
    if x % 2:
        print(x, 'is odd number')
    else:
        print(x, 'is even number')

even_odd(10)
even_odd(11)