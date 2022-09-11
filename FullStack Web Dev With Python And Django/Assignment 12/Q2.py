# 2. Write a python script to check whether a given number is Prime or not
n = int(input('Enter a number : '))

i = 2
for i in range(2, n):
    if n % i == 0:
        print('Not prime')
        break
    i += 1
else:
    print('Prime Number')
