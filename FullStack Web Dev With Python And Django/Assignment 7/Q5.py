# 5. Write a program which takes a number from user.
# Print Saurabh Shukla if the number is even,
# Print Prateek Jain if the number is negative odd number and
# Print Aditya Choudhary if number is positive odd number.

x = int(input('Enter a number: '))

match x:
    case x if x % 2 == 0:
        print('Saurabh Shukla')
    case x if x % 2 and x < 0:
        print('Pratik Jain')
    case x if x % 2 and x > 0:
        print('Aditya Chodhary')
