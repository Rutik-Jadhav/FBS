# Q5 WAP to print Fibonacci series upto n.


num = int(input('Enter the Number:'))

a = -1
b = 1
for i in range(num):
    c = a + b
    a = b
    b = c
    sum = c + i

print(f'The sum of the Fibonacci series upto {num} = {sum}')