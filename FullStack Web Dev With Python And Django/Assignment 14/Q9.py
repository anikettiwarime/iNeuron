# 9. Write a Python script to print indices of all occurrences of a given element in a given list.

li = [10, 20, 10, 30, 20, 40, 30, 20]
l2 = []

for i in li:
    if i not in l2:
        l2.append(i)


for j in l2:
    i = 0
    print(j, end=' : ')
    while i < len(li):
        if j == li[i]:
            print(i, end=' ')
        i += 1
    print()
