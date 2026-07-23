cost = int(input('Enter purchase amount:'))

if cost >= 1000:
    print('Discount: 20%\nTotal:',round(cost*0.8))
elif cost >= 500:
    print('Discount: 10%\nTotal:',round(cost*0.9))
elif cost < 500 and cost > 0:
    print('No discount available.\nTotal:',cost)
else:
    print('Invalid purchase amount.')