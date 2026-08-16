students ={
    'Harry': 'Gryffindor',
    'Ron': 'Gryffindor',
    'Hermione': 'Gryffindor',
    'Draco': 'Slytherin'
}

print(students['Harry'])
print(students['Ron'])
print(students['Hermione'])
print(students['Draco'])

#or
for student in students:
    print(student, students[student], sep=': ')
    