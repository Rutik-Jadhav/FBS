# Q7. Write a program to check if user has entered correct userid and password. 

userid = input('Enter the Username:')
password = input('Enter the Password:')

if(userid == 'Hrutik-123'):
    if(password == 'Hrutik@1202'):
        print('Login Successfully.')

    else:
        print('Incorrect Passsword.')

else:
    print('Incorrect Username.')

