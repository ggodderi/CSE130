# Python

import random

def bubble_sort2(numbers):
    count = 0
    for i in range(0, len(numbers), 1):
        for j in range(0, i):
            count += 1
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print(numbers, count)
    print(count)


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
    found = False
    count = 0
    while start <= end and not found:
        mid = find_middle_index(start, end)
        count += 1
        if selection == numbers[mid]:
            found = True 
        elif selection < numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return found, count, mid


def test_binary_search(numbers):
    for i in range(100):
        found, count, index = binary_search(numbers, i)
        print(f'Count is: {count}', end = ': ')
        if found:
            print(f'Found the number: {i}, at index: {index}')
        else:
            print(f'Number not found!')

def main():
    numbers = [ 23, 1, 45, 65, 89, 23, 1, 17, -12, 99, 14, 8, 27, 3]
    numbers2 = numbers.copy()

    bubble_sort(numbers)
    print(f'The sorted numbers are: {numbers}')

    # bubble_sort2(numbers2)
    # print(f'The sorted numbers are: {numbers2}')

    for i in range(100):
        random_numbers = [random.randint(1, 100) for _ in range(20)]
        bubble_sort(random_numbers)
        print(random_numbers)
    # numbers3 = [99,88,77,66,55,44,33,22,11,10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -99 ]
    # bubble_sort(numbers3)
    # print(numbers3)

    # test_binary_search(numbers)
    # test_binary_search(numbers2)


main()