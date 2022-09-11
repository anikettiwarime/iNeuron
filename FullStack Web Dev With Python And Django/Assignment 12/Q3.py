# 3. Write a python script to print all Prime numbers under 100


for n in range(2, 100):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)
