# 7. Write a python script to check whether a given number is positive, negative or zero.
x = int(input('Enter a number : '))

if x > 0:
    print(x, ' is positive')
elif x < 0:
    print(x, ' is negative')
else:
    print(x, ' is zero')
