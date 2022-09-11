# 3. Write a python script to calculate sum of cubes of first N natural numbers
n = int(input('Enter number : '))
sum_of_cube = 0

while n:
    sum_of_cube += n**3
    n -= 1

print('Cube : ', sum_of_cube)
