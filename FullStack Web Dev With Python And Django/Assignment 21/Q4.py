# 4. Write a recursive python function to print first N odd natural numbers in reverse order
def Print_N_Odd(n):
    if n == 0:
        return
    print(n*2-1, end=' ')
    Print_N_Odd(n-1)


Print_N_Odd(int(input('Enter any number : ')))
