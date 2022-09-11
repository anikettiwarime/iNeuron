# 8. Write a python script to calculate sum of digits of a given number
num = int(input('Enter number : '))

sum_of_digits = 0

while num:
    sum_of_digits += num % 10
    num //= 10

print('Sum of digits : ', sum_of_digits)
