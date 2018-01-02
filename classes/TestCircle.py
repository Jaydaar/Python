from Circle import Circle

def main():
    # Create a circle with radius 1
    circle1 = Circle()
    print("The area of the circle of radius {0:>3} is {1}.".format(circle1.radius, circle1.getArea()))

    # Create a circle with radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius {:>3} is {}.".format(circle2.radius, circle2.getArea()))

    # Create a circle with radius 125
    circle3 = Circle(125)
    print()
    print("The area of the circle of radius {:>3} is {}.".format(circle3.radius, circle3.getArea()))

    # Modify circle radius
    circle2.radius = 100 # or circle2.setRadius(100)
    print("The area of the circle of radius {:>3} is {}.".format(circle2.radius, circle2.getArea()))

main()