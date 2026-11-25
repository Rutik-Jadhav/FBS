# Q6. Write a program to print first n prime numbers.


num = int(input('Enter the Number:'))

for var in range(1, num+1):
    for j in range(2, var):
        if(var%j==0):
            break

    else:
        print(var)