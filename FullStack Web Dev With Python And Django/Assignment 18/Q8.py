# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

l1 = [1, 2, 3, 4]
l2 = ['Aniket', 'Prathmesh', 'Akshay', 'Nishant']
d = {}

for i in range(len(l1)):
    d[l1[i]] = l2[i]

print(d)
