
# # Серіалізація об'єктів в Python простий приклад
# # серіалізували та словник expenses
# expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}

# file_name = "expenses.txt"
# with open(file_name, "w") as fh:
#     for key, value in expenses.items():
#         fh.write(f"{key}|{value}\n")


# # десеріалізували словник expenses
# file_name = "expenses.txt"
# expenses = {}

# with open(file_name, "r") as fh:
#     raw_expenses = fh.readlines()
#     for line in raw_expenses:
#         key, value = line.split("|")
#         expenses[key] = int(value)

# print(expenses)


# import pickle

# # Об'єкт для серіалізації
# my_data = {"key": "value", "num": 42}

# # Серіалізація об'єкта в байтовий рядок
# serialized_data = pickle.dumps(my_data)
# # Виведе байтовий рядок
# print(serialized_data)  

# # Десеріалізація об'єкта з байтового рядка
# deserialized_data = pickle.loads(serialized_data)
# # Виведе вихідний об'єкт Python
# print(deserialized_data)



# import pickle
# # Після виконання коду ми збережемо словник **data** у файл
# # Об'єкт для серіалізації
# my_data = {"key": "value", "num": 100}

# # Серіалізація об'єкта в файл
# with open("data.pickle", "wb") as file:
#     pickle.dump(my_data, file)



# # Десеріалізацію даних з цього файлу
# import pickle

# # Десеріалізація об'єкта з файлу
# with open('data.pickle', 'rb') as file:
#     deserialized_data = pickle.load(file)

# # Виведе вихідний об'єкт Python
# print(deserialized_data)


# # Серіалізуємо екземпляр класу Human:

# import pickle

# class Human:
#     def __init__(self, name):
#         self.name = name

# bob = Human("Bob")
# with open("instance.pickle", "wb") as file:
#     pickle.dump(bob, file)

# """Важливо, щоб клас Human був визначений у скрипті,
# який виконує десеріалізацію, із тією ж структурою та
# в тому ж просторі імен, що й у скрипті, який виконав серіалізацію."""

# import pickle

# class Human:
#     def __init__(self, name):
#         self.name = name

# with open("instance.pickle", "rb") as file:
#     loaded_instance = pickle.load(file)

# print(loaded_instance.name)



# """
# Серіалізація об'єкта Python у рядок формату JSON виконується
# за допомогою методу json.dump(), якщо потрібно записати JSON безпосередньо у файл."""

# import json

# # Python об'єкт (словник)
# data = {"name": "Gupalo Vasyl", "age": 30, "isStudent": True}

# # Серіалізація у файл
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f)

# """
# Десеріалізація перетворює рядок у форматі JSON назад у відповідні об'єкти Python.
# Це виконується за допомогою методу json.load(), якщо JSON читається безпосередньо з файлу.
# """  
# import json

# # Десеріалізація з файлу
# with open("data.json", "r", encoding="utf-8") as f:
#     data_from_file = json.load(f)
#     print(data_from_file)



# """
# Створюемо обгортку для списку словників та зчитуємо створений файл
# """
# def write_contacts_to_file(filename, contacts):
#     with open(filename, "w") as file:
#         json.dump({"contacts": contacts}, file) 
 
    


# def read_contacts_from_file(filename):
#     with open(filename, "r") as file:
#         unpack = json.load(file)
        
#         return unpack["contacts"]





# """
# Ось як можна виправити та записати дані в файл JSON, використовуючи кирилицю:
# """
# import json

# # Python об'єкт (словник)
# data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# # Серіалізація у файл
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)



# """
# Для читання даних з CSV файлу можна використовувати функцію csv.reader, 
# що повертає об'єкт, який ітерує по рядках файлу.
# """
# import csv

# # Відкриваємо CSV файл
# with open("data.csv", newline="", encoding="utf-8") as csvfile:
#     # Створюємо об'єкт reader
#     reader = csv.reader(csvfile, delimiter=",")
#     # Проходимося по кожному рядку у файлі
#     for row in reader:
#         print(", ".join(row))



# """
# Для запису даних у CSV файл можна використати функцію csv.writer.
# Вона дозволяє легко записувати рядки даних у файл"""
# import csv

# # Дані для запису
# rows = [
#     ["name", "age", "specialty"],
#     ["Василь Гупало", 30, "Математика"],
#     ["Марія Петренко", 22, "Фізика"],
#     ["Олександр Коваленко", 20, "Інформатика"],
# ]

# # Відкриваємо файл для запису
# with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
#     # Створюємо об'єкт writer
#     writer = csv.writer(csvfile, delimiter=",")
#     # Записуємо рядки даних
#     writer.writerows(rows)


# """
# Модуль csv також надає класи csv.DictReader і csv.DictWriter,
# які дозволяють працювати з рядками як зі словниками. 
# Це зручно, коли у файлі CSV є заголовки стовпців."""

# import csv

# # Запис у CSV файл зі словників
# with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
#     fieldnames = ["name", "age", "specialty"] # є списком назв полів
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # створює об'єкт для запису

#     writer.writeheader() #записує рядок заголовків у файл
#     writer.writerow({"name": "Олег Олегов", "age": 23, "specialty": "Історія"}) # використовується для запису кожного рядка даних у файл
#     writer.writerow({"name": "Анна Сергіївна", "age": 22, "specialty": "Біологія"})

# # Читання з CSV файлу в словники
# with open("students.csv", newline="", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile) # створює об'єкт для ітерації по рядках файлу
#     for row in reader:
#         print(row["name"], row["age"], row["specialty"]) # кожен row є словником, де можна доступитися до значень полів за їхніми іменами


        
# import pickle

# class Robot:
#     def __init__(self, name, battery_life):
#         self.name = name
#         self.battery_life = battery_life
#         # Цей атрибут ми не збираємось серіалізувати
#         self.is_active = False  

#     def __getstate__(self):
#         state = self.__dict__
#         # Видаляємо is_active з серіалізованого стану
#         del state['is_active']
#         return state

#     def __setstate__(self, state):
#         # Відновлюємо об'єкт при десеріалізації
#         self.__dict__.update(state)
#         # Задаємо значення is_active за замовчуванням
#         self.is_active = False  




# """
# Методи __getstate__ і __setstate__ в Python дозволяють нам контролювати,
# як об'єкт повинен бути серіалізований та десеріалізований модулем pickle.
# """
# import pickle

# class Robot:
#     def __init__(self, name, battery_life):
#         self.name = name
#         self.battery_life = battery_life
#         # Цей атрибут ми не збираємось серіалізувати
#         self.is_active = False  

#     def __getstate__(self):
#         state = self.__dict__
#         # Видаляємо is_active з серіалізованого стану
#         del state['is_active']
#         return state

#     def __setstate__(self, state):
#         # Відновлюємо об'єкт при десеріалізації
#         self.__dict__.update(state)
#         # Задаємо значення is_active за замовчуванням
#         self.is_active = False  

# # Створення об'єкта Robot
# robot = Robot("Robo1", 100)

# # Серіалізація об'єкта
# serialized_robot = pickle.dumps(robot)

# # Десеріалізація об'єкта
# deserialized_robot = pickle.loads(serialized_robot)

# print(deserialized_robot.__dict__)


# """
# .__dict__,  є спеціальним атрибутом об'єкта, що містить словник з усіма 
# атрибутами, які належать до цього об'єкта. Ключі у цьому словнику 
# відповідають іменам атрибутів, а значення — це відповідні значення цих атрибутів
# """
# class Example:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj = Example("Gupalo Vasyl", 30)


# obj.__dict__['city'] = 'Poltava'  # Додавання нового атрибута
# print(obj.city)  # Виведення: Poltava

# del obj.__dict__['age']  # Видалення атрибута age
# print(obj.__dict__)  # Виведення: {'name': 'Gupalo Vasyl', 'city': 'Poltava'}


"""
Для того, щоб зробити екземпляри класу Reader серіалізованими, 
нам необхідно реалізувати методи __getstate__ та __setstate__ та керувати 
поведінкою pickle для класу. Це дозволить нам явно визначити, яка частина 
об'єкта має бути серіалізована, та як об'єкт має бути відновлений.
"""

import pickle

class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__, "fh": None}
        return attributes

    def __setstate__(self, state):
        # Відновлюємо стан об'єкта
        self.__dict__ = state
        self.fh = open(state["filename"], "r", encoding="utf-8")

if __name__ == "__main__":
    reader = Reader("data.txt")
    data = reader.read()
    print(data)
    reader.close()

    # Приклад серіалізації об'єкта Reader
    with open("reader.pkl", "wb") as f:
        pickle.dump(reader, f)

    # Приклад десеріалізації об'єкта Reader
    with open("reader.pkl", "rb") as f:
        loaded_reader = pickle.load(f)
        print(loaded_reader.read())
        loaded_reader.close()


