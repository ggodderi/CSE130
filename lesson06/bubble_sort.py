import random

def bubble_sort(numbers):
    loop_counter = 0
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            loop_counter += 1
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                # print(numbers)
    return loop_counter

def create_random_numbers_list(size):
    random_numbers = []
    for i in range(size):
        random_numbers.append(random.randint(0, 1000))
    return random_numbers

def main():
    data = [1, 3, 9, 3, 2, -1, 10, 9, -4, 7]
    bubble_sort(data)
    print(data)

    numbers = create_random_numbers_list(16)
    counts = bubble_sort(numbers)
    print(numbers)
    print(16, counts)
    numbers2 = create_random_numbers_list(32)
    counts = bubble_sort(numbers2)
    print(numbers2)
    print(32, counts)
    
    start = 2
    while start <= 64:
        numbers2 = create_random_numbers_list(start)
        counts = bubble_sort(numbers2)
        print(numbers2)
        print(start, counts)
        start *= 2



main()