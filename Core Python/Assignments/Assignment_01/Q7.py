# Q7. Program to Find the Roots of a Quadratic Equation

a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))



r1 = (-b + (b**2 - 4*a*c)**0.5)/2*a 
r2 = (-b - (b**2 - 4*a*c)**0.5)/2*a 



print(f'The roots of Quadratic Equation are {r1},{r2}')