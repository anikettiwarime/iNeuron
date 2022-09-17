# 5. Write a recursive python function to print first N even natural numbers.
def Print_N_Odd(n):
    if n == 0:
        return
    Print_N_Odd(n-1)
    print(n*2, end=' ')


Print_N_Odd(int(input('Enter any number : ')))
