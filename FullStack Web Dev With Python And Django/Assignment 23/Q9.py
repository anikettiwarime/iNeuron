# 9. Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter or triangle.
# Define and apply a decorator which checks for the validity of the triangle on the basis of lengths of the side.
# This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides.

def decor_peri(peri_fun):
    def Valid_Triangle(a, b, c):
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            print('Invalid Triangle')
            return
        else:
            print('Valid Triangle ')
            return peri_fun(a, b, c)

    return Valid_Triangle


@decor_peri
def perimeter_of_triangle(a, b, c):
    print("Perimeter of triangle : ", a+b+c)


x, y, z = int(input("Enter 1st side of triangle :")), int(input(
    "Enter 2nd side of triangle :")), int(input("Enter 3rd side of triangle :"))

perimeter_of_triangle(x, y, z)
