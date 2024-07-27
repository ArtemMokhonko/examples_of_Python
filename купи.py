import heapq


"""функція heapify перетворює ітерабельний об'єкт у купу."""
# nums = [1, 10, 3, 5, 4]
# heapq.heapify(nums)
# print(nums)  # Output: [1, 4, 3, 5, 10]


# heapq.heappush(nums, 0)
# print(nums)  # Output: [0, 4, 1, 5, 10, 3]

# min_elem = heapq.heappop(nums)
# print(min_elem)  # Output: 0
# print(nums)  # Output: [1, 4, 3, 5, 10]


# min_elem = heapq.heappushpop(nums, 10)
# print(min_elem)  
# print(nums)  

"""
реалізація пірамідального сортування за допомогою модуля heapq:
складність пірамідального сортування становить O(n*log*n)
"""
# import heapq

# def heap_sort(iterable, descending=False):
#     # Визначаємо, який знак використовувати залежно від порядку сортування
#     sign = -1 if descending else 1

# 		# Створюємо купу, використовуючи заданий порядок сортування
#     h = [sign * el for el in iterable]
#     heapq.heapify(h)
#     # Витягуємо елементи, відновлюємо їхні оригінальні значення (якщо потрібно) і формуємо відсортований масив
#     return [sign * heapq.heappop(h) for _ in range(len(h))]

# # Приклади використання функції
# arr = [12, 11, 13, 5, 6, 7]
# # Сортування за зростанням (за замовчуванням)
# sorted_arr_asc = heap_sort(arr)
# print("Відсортований масив (за зростанням):", sorted_arr_asc)
# # Сортування за спаданням
# sorted_arr_desc = heap_sort(arr, descending=True)
# print("Відсортований масив (за спаданням):", sorted_arr_desc)


import heapq

def min_cost_to_connect_cables(cables):
    # Створити мін-кучу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        # Витягнути два найменші елементи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднати їх
        new_cable = first + second
        
        # Додати новий кабель назад у купу
        heapq.heappush(cables, new_cable)
        
        # Додати вартість злиття до загальної вартості
        total_cost += new_cable
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cables))

