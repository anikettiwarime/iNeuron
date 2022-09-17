# 3. Write a recursive python function to print first N odd natural numbers
def Print_N_Odd(n):
    if n == 0:
        return
    Print_N_Odd(n-1, end=' ')
    print(n*2-1)


Print_N_Odd(int(input('Enter any number : ')))
