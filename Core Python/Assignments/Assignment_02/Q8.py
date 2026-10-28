# Q8. Write a program to swap two numbers using third variable. 

a = int(input('Enter the a value:'))
b = int(input('Enter the b value:'))


temp = a
a = b
b = temp

print(f'The swap value for a is {a}.')
print(f'The swap value for b is {temp}')