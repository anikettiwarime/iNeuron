# 5. Write a python script to print two given words in dictionary order
x = input('Enter word 1 : ')
y = input('Enter word 2 : ')

if x < y:
    print(x, y, sep=' ')
else:
    print(y, x, sep=' ')
