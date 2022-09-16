# 8. Write a python program to create a function that accepts a string and calculate the
# number of upper case letters and lower case letters.

def count_upper_case_char(s):
    c = 0

    for i in s:
        if i.isupper():
            c += 1

    return c


print("ANikeT has ", count_upper_case_char('ANikeT'), 'uppercase characters')
