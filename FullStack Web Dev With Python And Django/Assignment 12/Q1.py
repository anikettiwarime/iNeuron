# 1. Write a python script to reverse a number.
n = int(input('Enter a number : '))

while n:
    print(n % 10, end='')
    n //= 10
