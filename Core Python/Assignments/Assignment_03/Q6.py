# Q6. Write a program to calculate profit or loss. 

#sp = selling price and cp = cost price.
sp = float(input('Enter the selling price:'))
cp = float(input('Enter the cost price:'))

if(sp > cp):
    print('Your in profit.')

elif(cp > sp):
    print('Your in loss.')

else:
    print('zero net profit and zero net loss.')
    