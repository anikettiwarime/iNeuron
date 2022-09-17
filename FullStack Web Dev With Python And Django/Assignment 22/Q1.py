# 1. Write a recursive python function to calculate sum of first N natural numbers

def SumN(n):
    if n == 1:
        return 1
    s = n + SumN(n-1)
    return s


print(SumN(10))
