# Q11. Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition : 
#a. Children below 12 = 30% discount 
#b. Senior citizen (above 59) = 50% discount 
#c. Others need to pay full. 


age1 = int(input('Enter the age of 1st person:'))
age2 = int(input('Enter the age of 2nd person:'))
age3 = int(input('Enter the age of 3rd person:'))
age4 = int(input('Enter the age of 4th person:'))
age5 = int(input('Enter the age of 5th person:'))

amount = int(input('Ente the ticket amount:'))
# Total ticket amount
total_amount = amount*5

# Calculating discount for the first person.
if(age1 <= 12):
    dicount_price1 = (amount*70)/100
    print('30% Discount is applied...')
    print(f'Discount Price for 1st person is {dicount_price1}.')

elif(age1 >= 59):
    dicount_price1 = (amount*50)/100
    print('50% Discount is applied...')
    print(f'Discount Price for 1st person is {dicount_price1}.')

else:
    dicount_price1 = amount
    print(f'1st person need to pay full amount {dicount_price1}.')



# Calculating discount for second person.
if(age2 <= 12):
    dicount_price2 = (amount*70)/100
    print('30% Discount is applied...')
    print(f'Discount Price for 2nd person is {dicount_price2}.')

elif(age2 >= 59):
    dicount_price2 = (amount*50)/100
    print('50% Discount is applied...')
    print(f'Discount Price for 2nd person is {dicount_price2}.')

else:
    dicount_price2 = amount
    print(f'2nd person need to pay full amount {dicount_price2}.')


# Calculating discount for third person.
if(age3 <= 12):
    dicount_price3 = (amount*70)/100
    print('30% Discount is applied...')
    print(f'Discount Price for 3rd person is {dicount_price3}.')

elif(age3 >= 59):
    dicount_price3 = (amount*50)/100
    print('50% Discount is applied...')
    print(f'Discount Price for 3rd person is {dicount_price3}.')

else:
    dicount_price3 = amount
    print(f'3rd person need to pay full amount {dicount_price3}.')


# Calculating discount for fourth person.
if(age4 <= 12):
    dicount_price4 = (amount*70)/100
    print('30% Discount is applied...')
    print(f'Discount Price for 4rd person is {dicount_price4}.')

elif(age4 >= 59):
    dicount_price4 = (amount*50)/100
    print('50% Discount is applied...')
    print(f'Discount Price for 4rd person is {dicount_price4}.')

else:
    dicount_price4 = amount
    print(f'4th person need to pay full amount {dicount_price4}.')


# Calculating discount for fifth person.
if(age5 <= 12):
    dicount_price5 = (amount*70)/100
    print('30% Discount is applied...')
    print(f'Discount Price for 5rd person is {dicount_price5}.')

elif(age5 >= 59):
    dicount_price5 = (amount*50)/100
    print('50% Discount is applied...')
    print(f'Discount Price for 5rd person is {dicount_price5}.')

else:
    dicount_price5 = amount
    print(f'5th person need to pay full amount {dicount_price5}.')




total_discount_amount = dicount_price1 + dicount_price2 + dicount_price3 + dicount_price4 + dicount_price5

print(f'Total Discount price is {total_discount_amount}.')