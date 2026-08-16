students = ['Harry','Ron','Hermione']

print(students[0])
print(students[1])
print(students[2])

#or
for student in students:
    print(student)

    #or
for i in range(len(students)):
    print(students[i])

    #or rank students

for i in range(len(students)):
    print(i + 1, students[i])
    