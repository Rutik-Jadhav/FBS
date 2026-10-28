# Q4. WAP to calculate area of triangle and rectangle.

height = float(input('Enter the height:'))
width = float(input('Enter the width:'))
base = float(input('Enter the Base:'))
#area of rectangle.
rectangle = height*width

#area of triangle.
triangle = 1/2 * height*base

print(f'The area of Rectangle is {rectangle} and The area of triangle is {triangle}.')