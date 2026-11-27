# Q2. Write a program to find factorial of given number using recursion

def fact(n):
    if (n == 0):
        return 1
    else:
        return n * fact(n - 1)

n = int(input('enter number: '))

res = fact(n)
print('factorial is:', res)