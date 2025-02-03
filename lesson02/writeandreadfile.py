# python
try:
    with open("myname.txt", 'wt') as filehandle:
        filehandle.write("Uncle Bob\n")
except (FileExistsError, FileNotFoundError):
    print('File not found')

try:
    with open("myname2.txt", 'rt') as filehandle:
        name = filehandle.read()    
        print(f'your name is: {name}')
except (FileExistsError, FileNotFoundError):
    print('File not found')
