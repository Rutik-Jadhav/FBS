# Q4. Write a program to print pattern
# 10101
# 01010
# 10101
# 01010
# 10101

for i in range(5):
    for j in range(5):
        print((i + j) % 2, end="")
    print()