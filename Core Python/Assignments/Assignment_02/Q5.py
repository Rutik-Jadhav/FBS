# Q5. WAP to calculate selling price of book based on cost price and discount. 
# Take input for cost price and discount.
cost_price= float(input('Enter the cost price of a book:'))
Discount = float(input('Enter the Discount in %:'))

selling_price = cost_price*((100-Discount)/100)

print(f'The selling price for given cost price and discount is:{selling_price}$.')