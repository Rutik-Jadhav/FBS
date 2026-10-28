#Q4. Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and exterior wall. (Note: 1. Below diagram is of two joint roos. 2. It is upper view of building.)

area = float(input('Enter the of area of wall:'))
cost1 = float(input('Enter the cost of the interior wall:'))
cost2 = float(input('Enter the cost of the Exterior wall:'))


total_interior_wall = area*8
total_exterior_wall = area*7

total_cost_of_interior_wall = total_interior_wall*cost1
total_cost_of_exterior_wall = total_exterior_wall*cost2

print(f'The total area for interior wall is: {total_interior_wall}.')
print(f'The total area for exterior wall is: {total_exterior_wall}.')
print(f'The total cost for interioe wall is: {total_cost_of_interior_wall}.')
print(f'The total cost for exterior wall is: {total_cost_of_exterior_wall}')