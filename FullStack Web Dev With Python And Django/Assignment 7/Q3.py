# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.

a = int(input('Enter  Num 1 : '))
b = int(input('Enter  Num 2 : '))
c = int(input('Enter  Num 3 : '))


print('a. Check whether a given set of three numbers are lengths of an isosceles triangle or not.\nb. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not.\nc. Check whether a given set of three numbers are equilateral triangle or not')

ch = input('Enter your choice : ')

match ch:
    case 'a':
        if a == b:
            print('Isosceles triangle')
        elif b == c:
            print('Isosceles triangle')
        elif a == c:
            print('Isosceles triangle')
        else:
            print('Isosceles triangle')
        pass
    case 'b':
        if a**2 == b**2 + c**2:
            print('Right angle triangle')
        elif b**2 == a**2 + c**2:
            print('Right angle triangle')
        elif c**2 == b**2 + a**2:
            print('Right angle triangle')
        else:
            print('Not a Right angle triangle')
    case 'c':
        if a == b == c:
            print('Given set of numbers are equilateral triangle')
        else:
            print('Given set of numbers are not equilateral triangle')
