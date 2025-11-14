#  Write a program to calculate area and perimeter of a triangle
#     by creating a function.

def triangle_area_perimeter(a, b, c, h):
    area = 0.5 * b * h
    perimeter = a + b + c
    return area, perimeter


# taking input
a = float(input("Enter side a: "))
b = float(input("Enter base b: "))
c = float(input("Enter side c: "))
h = float(input("Enter height h: "))

area, peri = triangle_area_perimeter(a, b, c, h)

print("Area of triangle:", area)
print("Perimeter of triangle:", peri)
