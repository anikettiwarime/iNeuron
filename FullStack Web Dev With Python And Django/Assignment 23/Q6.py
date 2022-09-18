# 6. Create a generator to produce first n prime numbers
x = int(input('Enter no of even elements you need to print : '))


def n_prime_gen(n):
    i = 0
    j = 2
    while i < n:
        for x in range(2, j):
            if j % x == 0:
                break

        else:
            yield j
            i += 1
        j += 1


for i in n_prime_gen(x):
    print(i, end=' ')
