# """
# Якщо нам потрібно зберегти оригінальний список my_list без змін 
# і створити новий список з квадратами елементів, то слід створити 
# копію списку перед його зміною або змінити функцію, щоб вона 
# повертала новий список з квадратами елементів, замість зміни 
# вхідного списку. Наприклад:
# """

# my_list = [1, 2, 3]

# def square_list(x: list):
#     return [el**2 for el in x]

# new_list = square_list(my_list)
# print(new_list)
# print(my_list)

# """
# Для списків та словників можна скористатися явним копіюванням:
# """
# my_list = [1, 2, 3]
# copy_list = my_list[:] # Копія через зріз для списків
# copy_list.append(4)
# print(my_list, copy_list)


# my_dict = {1: "a"}
# copy_dict = {**my_dict} # Копія через розпакування для словників
# copy_dict["new_key"] = "new_value"
# print(my_dict, copy_dict)


# """
# Поверхнева копія об'єктів Python
# З цього прикладу видно, що хоча copy_list 
# вже є новим об'єктом, але вкладений у нього словник 
# з індексом 2 — це один і той самий словник і в copy_list, і в my_list
# """

# import copy

# my_list = [1, 2, {"name": "Gupalo Vasyl"}]
# copy_list = copy.copy(my_list)
# copy_list[2]["age"] = 30
# print(my_list)
# print(copy_list)
# # Виведення:
# #[1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]
# #[1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]


# """
# Створення глибоких копій об'єктів Python
# Для створення глибокої копії використовуйте метод 
# deepcopy() модуля copy. Ця функція рекурсивно створює нові об'єкти.
# """
# import copy

# my_list = [1, 2, {"name": "Gupalo Vasyl"}]
# copy_list = copy.deepcopy(my_list)
# copy_list[2]["age"] = 30
# print(my_list)
# print(copy_list)

# #Виведення:
# # [1, 2, {'name': 'Gupalo Vasyl'}]
# # [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]


import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, count_save = 0, contacts: list[Person] = None ):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = count_save

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['fh'] = None
        return attributes
    

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3