# 8. Write a python script to print first N terms of a Fibonacci series
n = int(input('Enter a number :'))

first = 0
second = 1
next = 0

for i in range(n):
    print(first, end=' ')
    next = first + second
    first = second
    second = next
