# Q6. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle. 

side1 = float(input('Enter the first side of triangle:'))
side2 = float(input('Enter the second side of triangle:'))
side3 = float(input('Enter the third side of triangle:'))

if(side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
    if(side1==side2==side3):
        print('The triangle is Equilateral.')

    elif(side1 == side2 or side1 == side3 or side3 == side2):
        print('The triangle is Isosceles.')

    else:
        print('The triangle is Scalene.')

else:
    print('The triangle is invalide.')