# Q3. Write a program to input angles of a triangle and check whether triangle is valid or not. 

angle1 = int(input('Enter the Angle1 of triangle in degree:'))
angle2 = int(input('Enter the Angle2 of triangle in degree:'))
angle3 = int(input('Enter the Angle3 of triangle in degree:'))


sum = angle1 + angle2 + angle3

if (sum == 180):
    print('The triangle is valid.')

else:
    print('The triangle is not valid.')