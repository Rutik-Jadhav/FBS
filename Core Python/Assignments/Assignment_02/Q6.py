# Q6. WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic. 

#Take input as a basic salary.
basic = float(input('Enter the basic salary:'))

#the formula for DA, TA, & HRA.

da = (basic*10)/100
ta = (basic*12)/100
hra = (basic*15)/100


#total of all.

total_salary = basic + da + ta + hra

#printing all

print(f'The DA is {da}')
print(f'The TA is {ta}')
print(f'The HRA is {hra}')
print(f'The total salary is:{total_salary}')