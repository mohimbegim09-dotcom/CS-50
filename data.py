#Ask user for their name
name = input('what is your name?') #or just do next line
name = input('What is your name?').strip().title()

#Remove whitespace from string
name = name.strip()
#Capitalize user's name
name = name.capitalize()
#Capitalize all words 
name = name.title() #or


#Remove whitespace and capitalize user's name
name = name.strip().title()

#Split user's name into first and last name
first, last = name.split(' ')

#Say hello to user by his first name
print(f'hello, {first}')

#Say hello to user
print(f'hello, {name}')


