def main():
    hello('world')
    goodbye('world')


def hello(name):
    print(f'hello,{name}')

def goodbye(name):
    print(f'goodbye,{name}')

if __name__ == '__main__':# these lines are used 
    #if you want to import functions from this file 
    # to another without calling the main function there
    main()

# now i can create my own library of functions and
#  import them into other files.

# look at file say.py