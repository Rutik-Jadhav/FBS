# Q5. 

num = int(input('Enter the value:'))



a = num%10
num = num//10


b = num%10

num = num//10

if(a==num):
    print('given number is pallindrom.')

else:
    print('given number is not pallindrom.')