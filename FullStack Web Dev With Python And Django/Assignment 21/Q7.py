# 7. Write a recursive python function to print squares of first N natural numbers

def N_Square(n):
    if n == 1:
        print(n**2, end=' ')
        return
    N_Square(n-1)
    print(n**2, end=' ')


N_Square(int(input('Enter any number : ')))
