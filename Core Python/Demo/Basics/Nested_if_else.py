gender = input('Enter the gender (M/F):')
age = int(input('Enter the age:'))

if(gender=='M'):
    if(age >= 21):
        print('Boy is eligible for marriage.')

    else:
        print('Boy is not eligible for marrige.')

else:
    if(age >= 18):
        print('Girl is eligible for marrige.')

    else:
        print('Girl is not eligible.')