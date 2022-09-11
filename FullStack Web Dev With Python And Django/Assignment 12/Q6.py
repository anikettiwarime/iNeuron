# 6. Write a python script to print first N prime numbers
x = int(input('Enter a number : '))

for n in range(2, x):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)