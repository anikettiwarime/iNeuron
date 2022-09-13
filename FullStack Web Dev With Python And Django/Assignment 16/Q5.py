# 5. Write a python program to check if all items in the tuple are the same.
t2 = (100, 100, 100)

j = t2[-1]

for i in t2:
    if j != i:
        print('Not same values')
        break
else:
    print('Same')
