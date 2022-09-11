# 7. Write a python script to count digits in a given number
num = int(input('Enter number : '))

digits = 0

while num:
    num = num // 10
    digits += 1

print('There are ', digits, ' digits in the given number')
