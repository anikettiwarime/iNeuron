# 8. Write a recursive python function to print cubes of first N natural numbers
def N_Cube(n):
    if n == 1:
        print(n**3, end=' ')
        return
    N_Cube(n-1)
    print(n**3, end=' ')


N_Cube(int(input('Enter any number : ')))
