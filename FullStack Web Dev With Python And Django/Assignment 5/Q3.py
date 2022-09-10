# 3. Write a python script to swap data of two variables

x = int(input('Enter a number 1 : '))
y = int(input('Enter a number 2 : '))

print('X : ', x, ' Y : ', y, end=' \nAfter Swaping \n')

temp = x
x = y
y = temp

del temp

print('X : ', x, ' Y : ', y)
