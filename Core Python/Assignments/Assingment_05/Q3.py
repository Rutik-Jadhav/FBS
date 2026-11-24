# Q3. Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount 
# to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passengers = int(input('Enter the nuber of Passengers:'))
tickets = int(input('Enter the ticket Cost:'))

x = 1
dic = 0
total_amount = 0
while(x<=passengers):
    age = int(input('Enter the Age of Passcenger:'))

    if(age<=12):
        dic = (tickets*70)/100
        print(f'The discount price for {x} person: {dic}.')
    elif(age>=59):
        dic = (tickets*50)/100
        print(f'The discount price for {x} person: {dic}.')
    else:
        dic = tickets
        print(f'The {x} person need to pay full amount of {dic}.')

    total_amount = total_amount + dic
    x+=1

print(f'The Total Amount You Need Pay = {total_amount}.')