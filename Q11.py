# Q11. WAP to check if given number Strong Number.


num = int(input('Enter the number:'))

temp = num
sum = 0
while(temp>0):
    dig = temp % 10

    fact = 1
    for i in range(1, dig+1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10

if(sum == num):
    print('Strong Number.')
else:
    print('Not a Strong Number.')



