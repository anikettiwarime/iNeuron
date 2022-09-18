# 2. Create a generator to produce first n odd natural numbers

x = int(input('Enter no of odd elements you need to print : '))


def n_odd_gen(n):

    i = 1
    while i < (n*2):
        yield i
        i += 2


for i in n_odd_gen(x):
    print(i)
