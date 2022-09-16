# 1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
list1 = sorted([10, 10, 10, 15, 9, 15, 12, 16, 50])


def unique(l):
    temp_set = {e for e in l}

    return list(sorted(temp_set))


l = unique(list1)

print(list1)

print(l)
