# Python

# Program an event vs sentinel while loop

correct_password = 'Joshua'
# Ask the user to enter a valid password:

# Event:
print('Event: ')
password = ''
count = 0
while password != correct_password and count < 5:
    password = input(f'Tries Remaining: {5 - count}, Please enter your password: ')
    count += 1

if password != correct_password:
    print('Incorrect Password - account frozen . . .')
else:
    print('Welcome profressor Falken, want to play a game?')



# Senteniel:
print('Senteniel: ')
done = False
count = 0
while not done:
    password = input(f'Tries Remaining: {5 - count}, Please enter your password: ')
    if password == correct_password:
        done = True
    if count >= 4:
        done = True
    count += 1

if password != correct_password:
    print('Incorrect Password - account frozen . . .')
else:
    print('Welcome profressor Falken, want to play a game?')



# Counter Controlled:
print('Counter Controlled')
for i in range(5):
    password = input(f'Tries Remaining: {5 - i}, Please enter your password: ')
    if password == correct_password:
        break
    
if password != correct_password:
    print('Incorrect Password - account frozen . . .')
else:
    print('Welcome profressor Falken, want to play a game?')