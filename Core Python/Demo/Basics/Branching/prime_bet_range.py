beg = int(input('Enter beg of range:'))
end = int(input('Enter end of range:'))

for num in range(beg, end):
    if(num > 1):
        for i in range(2, num):
            if(num % i == 0):
                break

        else:
            print(num, end=' ')



# WAP to print first n prime number