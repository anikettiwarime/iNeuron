# 10. Write a python program to create a function to check whether a string is an anagram or not.

s1, s2 = input('Enter string 1 :').lower(), input('Enter string 2 :').lower()


def check_anagram(a, b):
    if (sorted(a) == sorted(b)):
        return "Strings are anagram"
    else:
        return "Strings are not anagram"


print(check_anagram(s1, s2))
