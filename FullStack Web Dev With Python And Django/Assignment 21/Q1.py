# 1. Write a recursive python function to print first N natural numbers.

def printN(n):
    if n == 0:
        return
    printN(n-1)
    print(n)


printN(int(input('Enter any number : ')))
