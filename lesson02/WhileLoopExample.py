# Python

# This file will test a while loop with different exits


response = 'go'
while not response.lower() == 'stop':
    response = input('Enter "stop" to quit ')


response = 'go'
while response.lower() != 'stop':
    response = input('Enter "stop" to quit ')