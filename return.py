def main():
    x = int(input('What is x?'))
    print('x squared is', square(x))

def square(n):
   return n * n #or
   return n ** 2 #or
   return pow(n, 2)

main()