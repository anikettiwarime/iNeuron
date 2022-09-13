# 8. Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))

t2 = [i for i in tuple1]

t2 = sorted(t2, key=lambda x: x[1])
t2 = tuple(t2)

print(t2)
