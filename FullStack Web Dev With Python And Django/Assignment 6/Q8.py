# 8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))

root = (b**2) - (4*a*c)

if root > 0:
    print('Given quadratic equation has two real & distinct roots')
elif root == 0:
    print('Given quadratic equation has real & equal roots')
else:
    print('Given quadratic equation has two imaginary roots')
