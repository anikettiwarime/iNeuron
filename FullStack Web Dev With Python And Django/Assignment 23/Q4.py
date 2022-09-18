# 4. Create a generator to produce squares of first N natural numbers
x = int(input('Enter no of even elements you need to print : '))


def n_square_gen(n):
    i = 1
    while i <= (n):
        yield i**2
        i += 1


for i in n_square_gen(x):
    print(i, end=' ')
