# Q6. Write a Program to input two angles from user and find third angle of the triangle.

angle1 = float(input('Enter the First Angle:'))
angle2 = float(input('Enter the Second Angle:'))

# Formula for finding third angle.
Third_angle = 180-(angle1+angle2)

print("The Third Angle is:",Third_angle)