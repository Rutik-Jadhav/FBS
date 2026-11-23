# Q2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. 
# Display all percentage and average percentage of students.

students = int(input('Enter the number of Students:'))

# percentage = 0
total_percentage = 0
for i in range(1, students+1):
    math = int(input('Enter the marks optend in Maths:'))
    physics = int(input('Enter the marks optend in physics:'))
    chemistry = int(input('Enter the marks optend in chemistry:'))
    history = int(input('Enter the marks optend in history:'))
    geography = int(input('Enter the marks optend in geography:'))

    sum = math + physics + chemistry + history + geography
    percentage = (sum/500)*100
    print(f'The marks in Percentage of student {i} = {percentage}%')

    total_percentage = total_percentage + percentage

avg_percentage = total_percentage/students
print(f'The Average percentage of all {students} students = {avg_percentage}%')

