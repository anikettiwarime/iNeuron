# 5. Write a python script to calculate sum of first N even natural numbers
n = int(input('Enter number : '))
sum_of_n_even = 0

while n:
    sum_of_n_even += n*2
    n -= 1

print('Sum of first n even : ', sum_of_n_even)