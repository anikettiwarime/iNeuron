# 3. Write a recursive python function to calculate sum of first N even natural numbers
def Sum_N_Even(n):
    if n == 0:
        return 0
    s = (n*2) + Sum_N_Even(n-1)
    return s


print(Sum_N_Even(4))
