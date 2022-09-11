# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
x, y = int(input('Enter a number 1 : ')), int(input('Enter a number 2 : '))

for n in range(x, y+1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)
