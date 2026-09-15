# create a program which calculate the area of a circle
from math import pi 
if __name__ == '__main__':
    radius = float(input("Radius of the circle  : "))
    print("The area if the circle with radius " + str(radius) + " is "+ str(pi * radius** 2))