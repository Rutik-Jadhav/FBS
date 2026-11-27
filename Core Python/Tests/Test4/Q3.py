# Q3. 

def pattern(n):
    print('*' * n)

    for i in range(n - 1):
        print(' ' * (n - i) + '*')

    print('*' * n)

pattern(20)