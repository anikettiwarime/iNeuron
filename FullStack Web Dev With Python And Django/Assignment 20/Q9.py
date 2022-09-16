# 9. Write a python program to create a function to check whether a string is a pangram or not.


def chech_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    for c in alphabet:
        if c not in s:
            return "Not a pangram"
    else:
        return "The string is pangram"


string = "The quick brown fox jumps over the lazy dog"

print(chech_pangram(string))
