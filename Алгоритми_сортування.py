def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j] 
    return lst

numbers = [8, 2, 1, 4, 5]
print(bubble_sort(numbers))


"""
Сортування вставками (Insertion sort). Часова складність — 𝑂(𝑛2)
"""
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

numbers = [5, 3, 8, 4, 2]
print(insertion_sort(numbers))


"""
Алгоритм прямого вибору (Selection Sort) Часова складність — 𝑂(𝑛2)
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numbers = [5, 3, 8, 4, 2]
print(selection_sort(numbers))


"""
Швидке сортування (Quick sort) (сортуванням Гоара)
Часова складність — 𝑂(𝑛⋅log𝑛) у середньому випадку, але O(n2) у найгіршому випадку
"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([7, 12, 3, 5, 8, 11, 20, 1, 6, 14]))


"""
Сортування злиттям (Merge sort) Часова складність 𝑂(𝑛⋅log𝑛)
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

print(merge_sort([7, 12, 3, 5, 8, 11, 20, 1, 6, 14]))


"""
Алгоритм сортування Шелла. Часова складність — 𝑂(𝑛2)
"""
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        print(f"GAP: =============={gap}===================")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            print(f"i: ----------------- {i} ----------------")
            print(f"Список на початку ітерації {i}: {arr}")
            print(f"j: {j}, temp: {temp}, gap: {gap}")
            print(f"Порівнюємо елементи: {arr[j - gap]} > {temp}")
            while j >= gap and arr[j - gap] > temp:
                print(
                    f"Виконано обмін в циклу while: значення {arr[j - gap]} замінило {arr[j]}"
                )
                arr[j] = arr[j - gap]
                print(f"Список змінився j: {j}: {arr}")
                j -= gap
                print(f"Змінили j вліво: {j}")
            print(f"В кінці циклу for: значення {temp} замінило {arr[j]}")
            arr[j] = temp
            print(f"Список на кінець ітерації {i}: {arr}")
        gap //= 2
        if gap == 0:
            print("Сортування завершено")
    return arr

numbers = [5, 3, 8, 4, 2]
# numbers = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(numbers))

"""
Алгоритм порозрядного сортування (Radix Sort)
"""