# 1. Use iter and next method to access all the elements of a given set using while loop

set1 = {10, 20, "aniket", 90, 1.56}

it = iter(set1)

while True:
    try:
        x = next(it)
        print(x)
    except:
        # exit(0)
        break
        pass
