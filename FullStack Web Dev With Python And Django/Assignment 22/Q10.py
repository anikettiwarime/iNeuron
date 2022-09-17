# 10. Write a recursive python function to find the Nth term of the Fibonacci series.

def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)


print(fib(1))
