# Python

try:
    with open("my_name.txt", "wt") as filehandle:
        filehandle.write('Gary Godderidge')
except (FileExistsError, FileNotFoundError):
    print("Error creating file.")
    

try:
    with open("my_name.txt", "rt") as filehandle:
        name = filehandle.read()
        print(f'Your name is: {name}')
except (FileNotFoundError, FileExistsError):
    print("File does not exist")