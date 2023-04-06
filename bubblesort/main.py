def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# Przykładowa lista do posortowania
numbers = [5, 3, 8, 4, 2, 77,1] 

# Wywołanie funkcji sortującej
sorted_numbers = bubble_sort(numbers)

# Wyświetlenie posortowanej listy
print(sorted_numbers)