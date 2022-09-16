# 7. Write a python program to sum all the numbers in a list.

li = [10, 20, 35, 9, 50]


def sum_of_list(l):
    sum = 0
    for i in l:
        sum += i
    print('Sum :', sum)


sum_of_list(li)
