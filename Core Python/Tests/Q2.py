# Q2. Write a program to calculate simple interest based on Principal, Rate and Time(SI = P*R*T/100)

Principal = int(input('Enter the Principal:'))
Rate = int(input('Enter the Rate:'))
Time = int(input('Enter the time:'))

si = Principal*Rate*Time/100

print(f'The simple interest is:{si}')