# 10. Write a recursive python function to print a number in reverse order.
def printNumRev(n):
    if n > 0:
        print(n % 10, end='')
        printNumRev(n=n//10)


printNumRev(123)
print()
printNumRev(120)
