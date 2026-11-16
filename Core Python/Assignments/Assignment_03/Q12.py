# Q12. Write a program to check if given 3 digit number is a palindrome or not. 

n = int(input('Enter the 3 digit number:'))

pali1 = n % 10
n = n // 10

pali2 = n % 10
n = n // 10

new = pali1
pali1 = n 
n = new

if(new == pali1):
    print('The three digit number is palindrome.')

else:
    print('The three digit number is not a palindrome.')