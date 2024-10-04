# Python

# Program an event vs sentinel while loop

# Ask the user to enter a valid age:

# Event:
print('Event: ')
age = -1
while age <= 0 or age >= 120:
    age = int(input('Please enter your age: '))


# Senteniel:
print('Senteniel: ')
done = False
while not done:
    age = int(input('Please enter your age: '))
    if age >= 0 or age <= 120:
        done = True
    

# Counter Controlled:
print('Counter Controlled')
for i in range(999999999):
    age = int(input('Please enter your age: '))
    if age >= 0 or age <= 120:
        break 
    