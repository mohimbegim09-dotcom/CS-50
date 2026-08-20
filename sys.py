import sys # the user has to enter an 
           #information before running a program

print('hello, my name is', sys.argv[1])

# but what if he doesn't enter any information? 
# then the program will give an error. 
# so we have to handle that error using try and except block

import sys

try:
    print('hello, my name is', sys.argv[1])
except IndexError:
    print('too few arguments')


# or to catch all errors we can meet

import sys

if len(sys.argv) < 2:
    print('too few arguments')
elif len(sys.argv) > 2:
    print('too many arguments')
else:
    print('hello, my name is', sys.argv[1])

#or we can use the sys.exit() function to exit the program 
# if the user doesn't enter any information

import sys

if len(sys.argv) < 2:
    sys.exit('too few arguments')
elif len(sys.argv) > 2:
    sys.exit('too many arguments')

print('hello, my name is', sys.argv[1])

# if the user enters too many words(name in our case) 
#and we want to say hello to all of the names

import sys

if len(sys.argv) < 2:
    sys.exit('too few arguments')

for arg in sys.argv[1:]:# this means we are going to start 
    #from the second argument and go till the last argument
    # the firs argument is the name of the program itself 
    # so we are going to skip that
    print('hello, my name is', arg) 