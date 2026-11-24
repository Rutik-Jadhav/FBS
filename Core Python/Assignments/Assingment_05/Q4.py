# Q4. WAP to print Armstrong number within a given range


n1 = int(input('Enter the starting of the range:'))
n2 = int(input('Enter the Ending of the range:'))
# count = 0
for i in range(n1, n2+1):
    temp = i
    count = len(str(i))
    sum = 0

    while(temp>0):
        dig = temp % 10
        sum = sum + dig**count
        temp = temp // 10

    if(sum == i):
        print(i)
