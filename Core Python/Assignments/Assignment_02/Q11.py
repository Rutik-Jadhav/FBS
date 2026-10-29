# Q11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. 

amount = int(input('Enter the Amount:'))


r500 = amount//500
amount=amount%500

r200 = amount//200
amount= amount%200

r100 = amount//100 
amount=amount%100

r50 = amount//50
amount=amount%50

r20 = amount//20
amount = amount%20

r10 = amount//10
amount=amount%10

total_notes = r500 + r200 + r100 + r50 + r20 + r10 



print(f'500 notes:{r500}.')
print(f'200 notes:{r200}.')
print(f'100 notes:{r100}.')
print(f'50 notes:{r50}.')
print(f'20 notes:{r20}.')
print(f'10 notes:{r10}.')

print(f'The minimum number notes needed is{total_notes}.')