# Q11. Write a program to calculate area of an equilateral triangle.#

#Take  a input of 'a' where 'a' is length of any side.


a = int(input("Enter the value of 'a':"))

#formula for equilateral triangle.
area = (3**0.5/4)*a**2

print('The area of equilateral triangle for given "a" is',area)