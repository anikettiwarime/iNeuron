# 8. Create an endless iterator using generator method to produce Prime numbers

def endless_prime_gen():
    i = 2
    while True:
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            yield i
        i += 1


it = endless_prime_gen()
prime_list = []

while True:
    x = input("Do you want to generate more prime no's [y/n] : ")
    if x != 'y':
        break
    else:
        x = next(it)
        print(x, end=' ')
        prime_list.append(x)

print(prime_list)
