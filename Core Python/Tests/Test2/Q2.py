# Write a program to accept 3 digit number. if first digit is double of second digit and half of third digit then display "yes, you have done it", otherwise display "plz try next time".

num = int(input('Enter the first digit:'))

a = num%10
num = num//10


b = num%10

num = num//10

if(num==b*2 and a==num*2):
   print('yes, you have done it.')

else:
    print('plz try next time.')
