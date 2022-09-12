# 2. Write a Python script to create a list of first N odd natural numbers.

n = int(input('Enter a number : '))

li = [x*2-1 for x in range(1, n+1)]

print(li)
