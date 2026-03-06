import inspect

def main():
    print(inspect.currentframe().f_code.co_name)
    print(inspect.currentframe())

    print(inspect.currentframe().f_lineno)

main()