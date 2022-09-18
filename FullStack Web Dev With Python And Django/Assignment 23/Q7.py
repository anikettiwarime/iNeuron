# 7. Create an endless iterator using generator method to produce terms of Fibonacci series

def endless_fib_gen():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f+s


it = endless_fib_gen()
fib_list = []

while True:
    x = input('Do you want to generate more fibonacci no [y/n] : ')
    if x != 'y':
        break
    else:
        x = next(it)
        print(x,end=' ')
        fib_list.append(x)

print(fib_list)
