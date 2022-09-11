# 1. Write a python script to calculate sum of first N natural numbers
n = int(input('Enter number : '))

sum = 0

while n:
    sum += n
    n -= 1

print('Sum : ', sum)