length = int(input('Enter the length:'))
breadth = int(input('Enter the breadth:'))


radius = breadth/2

area = (length*breadth)+ (1/2)*3.14*radius**2

perimeter = (2 * length) + breadth + (3.14 * radius)

print(f'The area of the following figure is:{area}')
print(f'The perimeter is:{perimeter}')