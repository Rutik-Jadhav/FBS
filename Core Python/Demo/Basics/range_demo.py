# n = int(input('enter the number:'))

# for i in range(n*10,n-1,-n):
#     print(i)

# for i in range(5):
#     print(i)


# i = 1
# for i in range(5):
#     i += 1
#     print(i)


# n = int(input('enter the number:'))

# temp = 0

# for i in range (1, n+1):
#     temp+=i
#     print(temp)

# fibonacci series

n = int(input('How may fibonacci number you want:'))

a = -1
b = 1

for i in range(n):
    c = a + b
    print(c, end=' ')
    a = b
    b = c