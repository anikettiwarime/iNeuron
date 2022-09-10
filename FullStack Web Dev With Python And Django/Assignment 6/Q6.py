# 6. Write a python script to check whether a given number is a three digit number or not.
x = int(input('Enter a number : '))

x = str(x)

if len(x) == 3:
    print(x, ' is 3 digit number')
else:
    print(x, ' is not 3 digit number')
