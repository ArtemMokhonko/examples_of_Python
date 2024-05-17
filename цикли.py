
"""
У прикладі літери алфавіту з alphabet виводяться в консоль по черзі, через пробіл.
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")

""" 
Користувач вводить рядок. 
Треба порахувати скільки символів в рядку та скільки пробілів в рядку
"""
# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")

"""
Функція Range
"""
for i in range(0, 8, 2): #Ітерація з кроком. Цей приклад виведе парні числа від 0 до 8
    print(i)

"""
Функція Enumerate
"""
some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)


"""
Цикли та словники
"""
numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers.keys(): # Перебираєте ключі словника
    print(key)

for val in numbers.values(): # Перебрати саме значення словника
    print(val) 

for key, value in numbers.items():# Перебрати пари ключ значення словника треба використати метод items
    print(key, value)




