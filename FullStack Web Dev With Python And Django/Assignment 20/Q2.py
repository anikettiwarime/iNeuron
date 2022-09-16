# 2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def check_prime(x):
    for i in range(2, x):
        if not x % i:
            return "Not prime number"
    else:
        return "Prime number"


print(check_prime(10))
print(check_prime(2))
print(check_prime(11))
