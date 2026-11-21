# Q12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input('Enter the number:'))
count = len(str(num))
temp = num
sum = 0
while(temp>0):
    dig = temp % 10
    sum = sum + dig**count
    temp = temp // 10
if(sum == num):
    print('It is Armstrong number.')

else:
    print('It is not a Armstrong number.')