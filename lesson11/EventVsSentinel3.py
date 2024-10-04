# Python

# Program an event vs sentinel while loop

correct_password = 'Joshua'
# Ask the user to enter a valid password:

# Event:
print('Event: ')
password = ''
while password != correct_password:
    password = input(f'Please enter your password: ')

print('Welcome profressor Falken, want to play a game?')

# Senteniel:
print('Senteniel: ')
done = False
while not done:
    password = input(f'Please enter your password: ')
    if password == correct_password:
        done = True

print('Welcome profressor Falken, want to play a game?')

# Counter Controlled:
print('Counter Controlled')
for i in range(999999999999999999):
    password = input(f'Please enter your password: ')
    if password == correct_password:
        break

print('Welcome profressor Falken, want to play a game?')