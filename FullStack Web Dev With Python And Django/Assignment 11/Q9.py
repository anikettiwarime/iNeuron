# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
num = int(input('Enter number : '))
binary = ''

while num:
    binary += str(num % 2)
    num //= 2

i = len(binary)

while i:
    print(binary[i-1], end='')
    i -= 1
