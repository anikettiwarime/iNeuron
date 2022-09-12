# 7. Write a Python script to remove all non int values from a list.

li = ["Aniket", 9, 3+11j, 8, 1, 5.6]

length = len(li)

i = 0

while i < length:
    if type(li[i]) != int:
        li.pop(i)
        length -= 1
        continue
    i += 1

print(li)
