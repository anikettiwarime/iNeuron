# 9. Write a recursive python function to print first N multiples of a given number.
def firstNMul(x, n):
    if n == 0:
        return

    firstNMul(x, n-1)
    print(x, "*", n, ":", n*x)


firstNMul(5, 10)
