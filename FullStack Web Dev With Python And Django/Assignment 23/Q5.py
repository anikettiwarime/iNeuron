# 5. Create a generator to produce first n terms of Fibonacci series
x = int(input('Enter no of even elements you need to print : '))


def n_fib_gen(n):
    i, f, s = 0, 0, 1
    while i < n:
        yield f
        i += 1
        f, s = s, f+s


for i in n_fib_gen(x):
    print(i,end=' ')
