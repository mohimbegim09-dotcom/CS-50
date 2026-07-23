# Ask user for their name
name = input('What is your name? ')

#Say hello to user
print('hello, ' + name) #or
print('hello,', name ) #or

print('hello, ', end='')
print(name) #or

print('hello, ', name, sep='')#or

print(f'hello, {name}')