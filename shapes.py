import math
shape = input("Choose the shape you want to use, \n triangle, rectangle, square, circle, semicircle, parallelogram, rhombus, trapezium, kite, to end the program type end \n Type here: ")
while shape !="end":
    if shape == "triangle":
        tri1 = int(input("Enter base of the triangle: "))
        tri2 = int(input("Enter the hight of the triangle: "))
        print("The area of the triangle is {}".format((tri1*tri2)/2))
        shape = input("Type your next shape: ")
    elif shape == "rectangle":
        rec1 = int(input("Enter the length of the first side of the rectangle: "))
        rec2 = int(input("Enter the length of the second side of the rectangle: "))
        print("The area of the rectangle is {}".format(rec1*rec2))
        shape = input("Type your next shape: ")
    elif shape == "square":
        squ1 = int(input("Enter the length of the side of the square: "))
        print("The area of the square is {}".format(squ1**2))
        shape = input("Type your next shape: ")
    elif shape == "circle":
        cir1 = int(input("Enter the radius of the circle: "))
        print("The area of the circle is {}".format(cir1**2)*math.pi)
        shape = input("Type your next shape: ")
    elif shape == "semicircle":
        sem1 = int(input("Enter the radius of the semicircle: "))
        print("The area of the semicircle is {}".format(((sem1**2)*math.pi)/2))
        shape = input("Type your next shape: ")
    elif shape == "parallelogram":
        par1 = int(input("Enter the base of the parallelogram: "))
        par2 = int(input("Enter the hight of the parallelogram: "))
        print("The area of the parallelogram is {}".format(par1*par2))
        shape = input("Type your next shape: ")
    elif shape == "rhombus":
        rho1 = int(input("Enter the diagonal of the rhombus: "))
        rho2 = int(input("Enter the other diagonal of the rhombus: "))
        print("The area of the rhombus is {}".format((rho1*rho2)/2))
        shape = input("Type your next shape: ")
    elif shape == "trapezium":
        tra1 = int(input("Enter the base of the trapezium: "))
        tra2 = int(input("Enter the other base of the trapezium: "))
        tra3 = int(input("Enter the hight of the trapezium: "))
        print("The area of the trapezium is {}".format(((tra1+tra2)/2)*tra3))
        shape = input("Type your next shape: ")
    elif shape == "kite":
        kit1 = int(input("Enter the diagonal of the kite: "))
        kit2 = int(input("Enter the other diagonal of the kite: "))
        print("The area of the kite is {}".format((kit1*kit2)/2))
        shape = input("Type your next shape: ")
    else:
        print("invalid choice, try checking you spelling, enter your choice again")
        shape = input("Type here: ")

