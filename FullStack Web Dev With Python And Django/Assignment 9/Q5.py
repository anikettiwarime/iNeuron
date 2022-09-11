# 5. Write a python script to print first N odd natural numbers in reverse order
i = int(input('Enter a number : '))

while i:
    print(i*2-1)
    i -= 1
