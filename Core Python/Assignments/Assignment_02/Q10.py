# Q10. Write a program to reverse three-digit number. 

num = int(input('Enter the three number:'))

remainder1 = num % 10

num = num//10

remainder2 = num % 10

num = num//10

remainder3 = num % 10

print(remainder1, remainder2 , remainder3)