# Python




def bubble_sort(numbers):
    count = 0
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            count += 1
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print(numbers, count)
    print(count)

def find_middle_index(start, end):
    return (end + start) // 2

def binary_search(numbers, selection):
    start = 0
    end = len(numbers) - 1
    mid = find_middle_index(start, end)
    found = False
    count = 0
    while start <= end and not found:
        # print(start, mid, end)
        count += 1
        if selection == numbers[mid]:
            found = True 
        elif selection < numbers[mid]:
            end = mid - 1
            mid = find_middle_index(start, end)
        else:
            start = mid + 1
            mid = find_middle_index(start, end)
    print(f'Count is: {count}', end = ': ')
    if found:
        print(f'Found the number: {selection}')
    else:
        print(f'Number not found!')

def main():
    numbers = [ 23, 1, 45, 65, 89, 23, 1, 17, -12, 99, 14, 8, 27, 3]

    bubble_sort(numbers)
    print(f'The sorted numbers are: {numbers}')

    numbers2 = [99,88,77,66,55,44,33,22,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -99 ]
    bubble_sort(numbers2)
    print(numbers2)

    for i in range(100):
        binary_search(numbers, i)
    
    for i in range(100):
        binary_search(numbers2, i)
        # assert len(numbers) == len_numbers

main()