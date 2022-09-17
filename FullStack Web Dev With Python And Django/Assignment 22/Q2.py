# 2. Write a recursive python function to calculate sum of first N odd natural numbers
def Sum_N_odd(n):
    if n == 0:
        return 0
    s = (n*2-1) + Sum_N_odd(n-1)
    return s


print(Sum_N_odd(4))
