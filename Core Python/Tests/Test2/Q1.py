# Q1. Write a program to accept year from and check if it is a leap year or not.

year = int(input('Enter the Year:'))

year = year%4

if(year == 0):
    if(year%100 and year == 0):
        if(year%400 and year ==0):
            print('Leap Year.')

        else:
            print('NOT a leap year.')

    else:
        print('Leap Year he.')

else:
    print('Lear year Nahi he bhai.')