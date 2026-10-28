# Q3. Convert distance given in feet and inches into meter and centimeter. 
#Taking input as feet and inches.

feet = float(input('Enter the value in feet:'))
inches = float(input('Enter thee value in inches:'))

#fomulas for feet into meter and inches into centimeter. 
meter = feet*0.3048
centimeter = inches * 2.54


print(f'Given feet in meter is {meter} and given inches in centimeter is {centimeter}')