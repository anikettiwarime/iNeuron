# 4. Write a python program to create a function that checks whether a passed string is palindrome or not.

def is_palindrome(x):
    l = len(x)-1

    for i in x:
        if not i == x[l]:
            return "Not palindrome"
        
        if (l == len(x)/2):
            break
        l -= 1
    return "Palindrome"


print(is_palindrome("ABABA"))
