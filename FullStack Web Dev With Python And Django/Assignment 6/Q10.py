# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
x = int(input('Enter number 1 : '))
y = int(input('Enter number 2 : '))
z = int(input('Enter number 3 : '))


if x > y:
    if x > z:
        print(x, 'is greater')
    else:
        print(z, 'is greater')
else:
    if y > z:
        print(y, 'is greater')
    else:
        print(z, 'is greater')
