# 5. Write a python script to print first N odd natural numbers in reverse order
n = int(input('Enter a number : '))

for i in range(n*2-1, 0, -2):
    print(i)
