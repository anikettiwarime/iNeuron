# 2. Write a python script to calculate sum of squares of first N natural numbers

n = int(input('Enter number : '))
sum_of_square = 0

while n:
    sum_of_square += n**2
    n -= 1

print('Square : ', sum_of_square)
