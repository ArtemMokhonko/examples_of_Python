# import pickle


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         pass
        
        
        
        


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
        
        
    
#     def save_to_file(self):
#         pass
        
            

#     def read_from_file(self):
#         pass


# allen =Person (
#     "Allen Raymond",
#     "nulla.ante@vestibul.co.uk",
#     "(992) 914-3792",
#     False,)

# contacts = [
#     Person(
#         "Allen Raymond",
#         "nulla.ante@vestibul.co.uk",
#         "(992) 914-3792",
#         False,
#     ),
#     Person(
#         "Chaim Lewis",
#         "dui.in@egetlacus.ca",
#         "(294) 840-6685",
#         False,
#     ),
# ]

# persons = Contacts("user_class.dat", contacts)

# print(persons)
# Просте форматування рядка

# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))


def discount_price(price:int, discount: float):
    def apply_discount():
        nonlocal price 
        apply_discount(price * (1 - discount))
        
        

    
    return price

res = discount_price(100, 0.5)
print(res)