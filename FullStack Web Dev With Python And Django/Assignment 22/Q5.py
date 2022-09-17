# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers
def Sum_N_Cube(n):
    if n == 1:
        return 1
    s = (n**3) + Sum_N_Cube(n-1)
    return s


print(Sum_N_Cube(2))
print(Sum_N_Cube(3))
print(Sum_N_Cube(4))
