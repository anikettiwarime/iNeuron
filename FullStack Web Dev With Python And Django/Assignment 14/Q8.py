# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
li = [10, 20, 10, 20, 30, 30, 30, 40]

# print(li.count(10))
# print()

l2 = []
a = 0

for i in li:
    if i not in l2:
        l2.append(i)
        print(i, li.count(i))
