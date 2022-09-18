# 10. Define a function which calculates HCF of two numbers.
# Define and apply a decorator to check whether two given numbers are co-prime or not .

x, y = int(input('Num 1 :')), int(input('Num 2 :'))


def decor_hcf(hcf):
    def co_prime(x, y):
        for i in range(2, max(x, y)):
            if x % i == 0 and y % i == 0:
                print('Not a Co-prime')
                return hcf(x, y)
        else:
            print('Co-prime')

    return co_prime


@decor_hcf
def hcf(x, y):
    while y:
        x, y = y, x % y  # euclids theorem
    print('because hcf is :', x)


hcf(x, y)
