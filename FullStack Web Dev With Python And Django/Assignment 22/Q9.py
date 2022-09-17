# 9. Write a recursive python function to print octal of a given decimal number
def print_N_Octal(n):
    if n > 0:
        print(n % 8, end='')
        print_N_Octal(n//8)


print_N_Octal(3)
