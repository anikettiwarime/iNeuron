# 5. Write a python script to find next prime number of a given number
x = int(input('Enter a number : '))

while True:
    x += 1
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x)
        break
