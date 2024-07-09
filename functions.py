# """ФУНКЦІЇ"""

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes

# result = string_to_codes("Hello world!")
# print(result)


# """
# Розрахунок реальної ціни з врахуванням дисконту
# """
# def real_cost(base: int, discount: float = 0) -> float: 
#     return base * (1 - discount) # Формула base * (1 - discount) для обрахунку остаточної вартості.
# price_bread = 15
# current_price_bread = real_cost(price_bread, 0.5)
# print(f'Нова вартість хліба: {current_price_bread}')



# """
# Приклад використання параметру *args
# Функція, яка буде передану будь яку кількість рядків
# об'єднувати в один рядок та повертати його
# """
# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result

# print(f"Hello", "world", "!")

# """
# Приклад використання параметру **kwargs
# """
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# greet(name="Alice", age=25 )

# """
# *args та **kwargs використання разом у функції
# """
# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)

# example_function(1, 2, 3, name="Alice", age=25)

# """
# Розпакування словників
# """
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)


# """
# Рекурсивна функція для обчислення факторіала
# """
# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# print(factorial(5)) # виведе 120


# """
# Приклад коду, який показує, як працює стек викликів
# у рекурсії на прикладі функції для обчислення факторіала числа
# """
# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# # for char in message:
# #     if char == search:
# #         result +=1
# result = ([result for char in message if char == search])
# result = len(result)

# print(result)

from functools import lru_cache

@lru_cache(maxsize=None)  # Unbounded cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(35)) 

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = value
        return value
print(fibonacci_memo(50))