
import inspect
import traceback

def my_assert(expression, message, error_code, 
              file_name, function_name, line_number):
    if (not expression):
        print(f'Assertion failed: function: {function_name}, file line number: {line_number}')
        print(f'File name: {file_name}')
        # print(f'Call Stack:{call_stack}')
        print(f'Error Code: {error_code}, Error Message: {message}')
        print('\nAssert Call Stack: ')
        traceback.print_stack()
        print('\nExiting program. . . ')
        exit(1)


def main():
    # print(type(inspect.stack()))
    # for item in inspect.stack():
    #     print(f'{item}\n\n\n\n\n')
    # stack = traceback.format_stack()
    # print(traceback.print_stack())
    # print(stack)

    my_assert(1>2, "Hello Bob", "10.20.30", __file__, 
              inspect.currentframe().f_code.co_name,
              inspect.currentframe().f_lineno)

main()