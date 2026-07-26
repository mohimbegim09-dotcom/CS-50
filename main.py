# You can use main() function to organize your code in a way you want to

def main():
    name = input('What is your name?')
    hello(name)

def hello(to = 'world'):                                                                
    print('hello,', to)

main()