def hello():
    print('hello')


name = input("Enter your name: ")
hello()
print(name)

#OR
def hello(to):
    print('hello,', to)

name = input("Enter your name: ")
hello(name)

# But if you dont want to put name into hello() function, 
#you can assign any other meaning, using this:
def hello(to="world"):
    print('hello,', to)


hello() # will print hello, world