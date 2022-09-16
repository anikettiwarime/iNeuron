# 9. Write a python program to merge two python dictionaries into one dictionary.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'A': 110, 'B': 210, 'C': 310}

for k, v in d2.items():
    d1[k] = v


print(d1)
