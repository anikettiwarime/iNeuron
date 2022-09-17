# 2. Write a recursive python function to print first N natural numbers in reverse order

def printNRev(n):
    if n == 1:
        print(n, end=' ')
        return
    print(n, end=' ')
    printNRev(n-1)


printNRev(int(input('Enter any number : ')))
