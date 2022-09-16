# 3. Write a python program to create a function that prints the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_even(l):
    for i in l:
        if not i % 2:
            print(i, end=' ')


print_even(li)
