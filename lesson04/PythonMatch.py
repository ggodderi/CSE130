# Python

# Test a python match statement.



command = input('Please input the first letter of the command (a-z/A-Z): ')

command = command.upper()

match command:
    case 'A': 
        print(f'Running the {command} command')
    case 'B': 
        print(f'Running the {command} command') 
    case 'C': 
        print(f'Running the {command} command')
    case 'D': 
        print(f'Running the {command} command')
    case 'E': 
        print(f'Running the {command} command')
    case 'F': 
        print(f'Running the {command} command')
    case 'G': 
        print(f'Running the {command} command')
    case 'H': 
        print(f'Running the {command} command')
    case 'I': 
        print(f'Running the {command} command')
    case 'J': 
        print(f'Running the {command} command')
    case _:
        print(f'Running the default command')

