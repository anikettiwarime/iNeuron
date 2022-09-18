# 3. Create a generator to produce first n even natural numbers
x = int(input('Enter no of even elements you need to print : '))


def n_even_gen(n):
    i = 2
    while i <= (n*2):
        yield i
        i += 2


for i in n_even_gen(x):
    print(i)
