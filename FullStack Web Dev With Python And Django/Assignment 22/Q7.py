# 7. Write a recursive python function to calculate sum of the digits of a given number

def fact(n):
    if n == 1:
        return 1
    f = n*fact(n-1)
    return f


print(fact(5))