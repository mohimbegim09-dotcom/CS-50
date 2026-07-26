x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

# IF i WANT TO ROUND THE ANSWER  
# formula:  round(number[, ndigits])
print(round(x + y))


#DIVISION
z = round(x / y)
print(z)
# to round
z = round(x / y, 2)
print(z)
# OR
z = x / y
print(f"{z:.2f}")


