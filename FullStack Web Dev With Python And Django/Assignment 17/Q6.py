# 6. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]

S = {"Python", "Django", "JavaScript"}
l = ["Java", "C"]

S.update(l)
print(S)