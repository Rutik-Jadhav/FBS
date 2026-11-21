# Q9. WAP to print all numbers in a range divisible by a given number.



num1 = int(input('Enter the number:'))
num2 = int(input('Enter the number:'))
div_num = int(input('Enter the divisible number:'))

for i in range(num1,num2+1):
    if(i%div_num==0):
        print(i)
    