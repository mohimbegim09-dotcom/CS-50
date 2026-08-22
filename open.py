name = input('What is your name?')

file = open('names.txt', 'a') #a for append
file.write(f'{name}\n')
file.close()

# or

with open('names.txt', 'a') as file:
    file.write(f'{name}\n')

    # to read the file with names you created

with open('names.txt', 'r') as file: #r for read
    lines = file.readlines()

for line in lines:
    print('hello, ', line, end='')
    #or
for line in lines:
    print('hello, ', line.rstrip())
    #rstrip means deleting an extra spces

    #or

with open('names.txt', 'r') as file:
    for line in file:
        print('hello,', line.rstrip())


        # to sort names

names = []

with open('names.txt') as file:
    for line in file:
        names.append(line.rstrip())

    for name in sorted(names):
        print(f'hello, {name}')

        #or

with open('names.txt') as file:
    for line in sorted(file):
        print('hello,', line.rstrip())


     # to sort in non alphabetical order

names = []

with open('names.txt') as file:
    for line in file:
        names.append(line.rstrip())

    for name in sorted(names, reverse=True):
        print(f'hello, {name}')