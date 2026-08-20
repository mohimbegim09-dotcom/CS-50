try:
    x = int(input('What is x?'))
    print(f'x is {x}')
except ValueError:
    print('x is not an integer')

    # or

try:
    x = int(input('What is x?'))
except ValueError:
    print('x is not an integer')
else:
    print(f'x is {x}')

    #or 

while True:
    try:
        x = int(input('What is x?'))
    except ValueError:
        print('x is not an integer')
    else:
        break

print(f'x is {x}')


 #or

def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            x = int(input('What is x?'))
        except ValueError:
            print('x is not an integer')
        else:
            return x

main()

#or

def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            return int(input('What is x?'))
        except ValueError:
            print('x is not an integer')

main()