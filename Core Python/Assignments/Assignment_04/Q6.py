# Q6. WAP to check if a given number is prime number or not.


num = int(input('Enter the Number:'))

for i in range(2, num):
    if(num % i ==0):
        print('is not a prime number.')
        break
else:
    print('is a prime number.')