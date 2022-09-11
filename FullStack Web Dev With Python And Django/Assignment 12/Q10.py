# 10. Write a python script to calculate HCF of two numbers
x, y = int(input('Num 1 :')), int(input('Num 2 :'))

i = 2
max = min(x, y)
while i <= max:
    if x % i == 0 and y % i == 0:
        print(i)
        break
    i += 1
else:
    print(1)
