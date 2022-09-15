# 5. Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"} secondset = {"C", "Cpp", "NoSQL"}

s1 = {"Java", "Python", "SQL"}
s2 = {"C", "Cpp", "NoSQL"}

s1.update(s2)

print(s1)