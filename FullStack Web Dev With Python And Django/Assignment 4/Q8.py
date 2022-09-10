# 8. Write a python script to calculate simple interest
p = float(input('Enter principal amount : '))
r = float(input('Enter rate of interest : '))
t = float(input('Enter time : '))

r = r/100
SI = p*r*t

print('Simple interest is : ', SI)
