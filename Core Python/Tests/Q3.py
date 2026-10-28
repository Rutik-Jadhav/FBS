# Q3. Write a program to accept distance in km and convert it into meters and centimeters both.

distance = float(input('Enter the distance in km:'))

# distance km into meters and centimeters.

meters = distance *1000

centimeters = distance*100000

print(f'meters:{meters} and centimeters:{centimeters}')