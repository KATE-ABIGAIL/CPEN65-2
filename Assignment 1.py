import math

def area_of_circle(radius):
    area_of_circle = 3.141592653589793238 * radius * radius
    return area_of_circle

radius = int(input("Input Radius: "))
print("The area of the circle is", area_of_circle(radius))