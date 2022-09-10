# 7. Write a python program to check whether a given number is positive, negative or zero using match case statement

x = int(input('Enter a number : '))

match x:
    case x if x > 0:
        print('Given number is positive')
    case x if x == 0:
        print('Given number is Zero')
    case x if x < 0:
        print('Given number is negative')
