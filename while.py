while True:
    n = int(input('What is n?'))
    if n < 0:
        continue
    else:
        break

    #or

while True:
    n = int(input('What is n?'))
    if n > 0:
        break

for _ in range(n):
    print('Meow!')
    