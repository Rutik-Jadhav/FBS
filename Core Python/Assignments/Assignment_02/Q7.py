# Q7. Find the sum of three-digit number. 

num = int(input('Enter the three digit number:'))

# take remender1
remender1 = num%10
num = num//10

# take remender2
remender2 = num%10
num = num//10

#take sum of reneders and input
sum = remender1 + remender2 + num

print(f'The sume of the all three digits is {sum}.')