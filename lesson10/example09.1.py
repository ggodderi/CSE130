# Python

income = -1

while income <= 0:
    income = float(input('Input your income: '))
    if income < 0:
        print('Please input a valid number > 0')
    
print(f'Your incoment is: {income}')




income = float(input('Input your income: '))
while income <= 0:
    print('Please input a valid number > 0')
    income = float(input('Input your income: '))

print(f'Your incoment is: {income}')