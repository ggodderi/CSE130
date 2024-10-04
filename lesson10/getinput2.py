# Python

DAY_INDEX = 0
MONTH_INDEX = 1
YEAR_INDEX = 2


def get_int_input_value(min, max, message):
    received_correct_input = False

    while not received_correct_input:
        try:
            value = int(input(message))
            if value < min or value > max:
                print(f'{value} is not correct, please enter int value between {min} and {max}')
            else:
                received_correct_input = True
        except ValueError as ve:
            print(f'Invalid Input: actual error {ve}, must input an integer.')
    return value


def validate_dates(start_date, end_date):
    if start_date[YEAR_INDEX] > end_date[YEAR_INDEX]:
        return False
    elif start_date[YEAR_INDEX] == end_date[YEAR_INDEX] and \
        start_date[MONTH_INDEX] > end_date[MONTH_INDEX]:
        return False
    elif start_date[YEAR_INDEX] == end_date[YEAR_INDEX] and \
         start_date[MONTH_INDEX] == end_date[MONTH_INDEX] and \
         start_date[DAY_INDEX] > end_date[DAY_INDEX]:
        return False
    else:
        return True
    

def get_input():
    received_correct_input = False

    while not received_correct_input:
        start_day = get_int_input_value(1, 31, "Please enter the Start Day: ")
        start_month = get_int_input_value(1, 12, "Please enter the Start Month: ")
        start_year = get_int_input_value(1753, 999999999, "Please enter the Start Year: ")

        end_day = get_int_input_value(1, 31, "Please enter the End Day: ")
        end_month = get_int_input_value(1, 12, "Please enter the End Month: ")
        end_year = get_int_input_value(1753, 999999999, "Please enter the End Year: ")


        start_date = (start_day, start_month, start_year)
        end_date = (end_day, end_month, end_year)

        print(start_date, end_date)

        received_correct_input = validate_dates(start_date, end_date)
        if not received_correct_input:
            print(f'Incorrect Input dates: start date must be before end date')
            print(f'start date:{start_date}, end date: {end_date}')
        else:
            received_correct_input = True
        # print(valid_dates)

    return start_date, end_date

def main():
    start_date, end_date = get_input()
    print(start_date, end_date)

main()
