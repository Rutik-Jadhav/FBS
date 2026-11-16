# Q10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18) 

gender = input('Enter the Gender (M/F):')
age = int(input('Enter your Age:'))

if(gender == 'M'):
    if(age >= 21):
        print('Your Eligible for marage...')

    else:
        print('Your Not Eligible for marage...')

elif(gender == 'F'):
    if(age >= 18):
        print('Your Eligible for marage...')

    else:
        print('Your Not Eligible for marage...')

else:
    print('Unkown Gender...')