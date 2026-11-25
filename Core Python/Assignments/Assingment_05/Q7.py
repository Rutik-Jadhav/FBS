# Q7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms


n = int(input('Enter the Number:'))
# a = int(input('Enter the Number a:'))
# N = int(input('Enter the Number:'))

# # a. 1! + 2! + 3! + 4! + .....n!
# x = 1
# fact = 0
# while(x<=n):
#     sum = 1
#     for i in range(1, x+1):
#         sum = sum * i
    
#     fact = fact + sum
#     x+=1
# print(fact)


# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

# expo = 1
# power = 0
# res = 0
# while(expo<=N):
#     power = N**expo
#     res = res + power
#     expo+=1
# print(res)

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

# a = 1
# sum_of_series = 0 
# for i in range(1, n+1):
#     a = a *2
#     sum_of_series = sum_of_series + a
#     print('b', a)
# print(sum_of_series)

# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
x = 1
s = 0
while(x<=10):
    s = s + (a*x)/x
    print(s)
    x+=1

# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
