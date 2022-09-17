# 8. Write a recursive python function to print binary of a given decimal number.

def printBinary(n):
    if n > 0:
        print(n % 2, end='')
        printBinary(n//2)


printBinary(3)
