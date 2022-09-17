# 4. Write a recursive python function to calculate sum of squares of first N natural numbers
def Sum_N_Square(n):
    if n == 1:
        return 1
    s = (n**2) + Sum_N_Square(n-1)
    return s


print(Sum_N_Square(2))
print(Sum_N_Square(3))
print(Sum_N_Square(4))
