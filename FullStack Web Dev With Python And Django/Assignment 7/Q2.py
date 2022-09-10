# 2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
a = int(input('Enter num 1 : '))
b = int(input('Enter num 2 : '))
print('\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division')

c = int(input('\nSelect operation you want to do : '))

match c:
    case 1:
        print('Addition : ', a+b)
    case 2:
        print('Subtraction : ', a-b)
    case 3:
        print('Multiplication : ', a*b)
    case 4:
        print('Division : ', a/b)
