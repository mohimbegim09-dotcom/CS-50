print('#')
print('#')
print('#')

#or
for _ in range(3):
    print('#')

#or

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print('#')

main()

#or

def main():
    print_column(3)

def print_column(height):
    print('#\n' * height, end='')

main()