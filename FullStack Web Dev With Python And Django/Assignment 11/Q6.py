# 6. Write a python script to calculate factorial of a given number
n = int(input('Enter number : '))
fact = 1

while n:
    fact *= n
    n -= 1

print('Factorial : ', fact)
