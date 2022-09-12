# 3. Write a Python script to create a list of first N even natural numbers.

n = int(input('Enter a number : '))

li = [x*2 for x in range(1, n+1)]

print(li)
