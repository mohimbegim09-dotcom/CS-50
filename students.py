with open('students.csv') as file:
    for line in file:
        row = line.rstrip().split(',')
        print(f'{row[0]} is in {row[1]}')

        #or
with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        print(f'{row[0]} is in {row[1]}')

# to sort by name

students = []

with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        students.append(f'{name} is in {house}')

for student in sorted(students):
    print(student)