# 7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
x, y = int(input('Num 1 :')), int(input('Num 2 :'))

for i in range(2, max(x, y)):
    if x % i == 0 and y % i == 0:
        print('Not a Co-prime')
        break
else:
    print('Co-prime')
