# 9. Write a Python script to create a list of city names taken from the user.
city = []

x = int(input("Enter number of cities you want to enter : "))

while x:
    city.append(input('Enter City name : '))
    x -= 1

print(city)
