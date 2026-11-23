# calculating travel tkt amount by using loops.

totalprice = 0 
i = 1
while(i<5):
    ag1 = int(input(f'Enter the age of {i}st person:'))
    tk1 = float(input(f'Enter the Amount of {i}st person:'))

    if(ag1 >= 59):
        disc = ((tk1*50)/100)
        totalprice = totalprice + tk1
        print(f'You will get dicount of {disc}.')

    elif(ag1 <= 12):
        disc = ((tk1*70)/100)
        totalprice = totalprice + tk1
        print(f'You will get dicount of {disc}.')

    else:
        totalprice = totalprice + tk1
        print(f'You need to pay full amount of {totalprice}.')

    i += 1
print(f'Tatal price for all tickets is {totalprice}.')