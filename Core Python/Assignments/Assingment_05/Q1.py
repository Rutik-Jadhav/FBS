# Q1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials.
#Let him try 3 times. After that program to terminate.

for i in range(1,4):
    id = int(input('Enter the Userid:'))
    password = input('Enter the Password:')

    if(id==3722121015):
        if(password=='Hrutik#06'):
            print('Login Successfully.')
            break
        else:
            print('Incorrect Password.')

    else:
        print('Incorrect Userid.')

