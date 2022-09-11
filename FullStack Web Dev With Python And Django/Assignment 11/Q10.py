# 10. Write a python script to print the octal equivalent of a given decimal number. (do notuse oct() method)
num = int(input('Enter number : '))
octal = ''

while num:
    octal += str(num % 8)
    num //= 8

i = len(octal)

while i:
    print(octal[i-1], end='')
    i -= 1
