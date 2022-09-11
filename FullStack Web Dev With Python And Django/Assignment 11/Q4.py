# 4. Write a python script to calculate sum of first N odd natural numbers
n = int(input('Enter number : '))
sum_of_n_odd = 0

while n:
    sum_of_n_odd += n*2-1
    n -= 1

print('Sum of first n: ', sum_of_n_odd)
