# 9. Write a python script to calculate LCM of two numbers
x, y = int(input('Num 1 :')), int(input('Num 2 :'))

maxNum = max(x, y)

while True:
    if maxNum%x ==0 and maxNum%y==0:
        print(maxNum)
        break
    maxNum+=1
