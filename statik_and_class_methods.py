
# Статичний метод, який обчислює площу кола, використовуючи переданий радіус
class Geometry:        
    PI = 3.14159

    @staticmethod
    def area_of_circle(radius):
        return Geometry.PI * radius ** 2
print(Geometry.area_of_circle(5))  


#___________________________________________________________________________________________
# Класовим методом, який дозволяє створювати екземпляри Employee,
# розбираючи рядок на поля. Метод використовує параметр cls  
# для створення нового екземпляра, гарантуючи, що він може бути 
# успішно використаний навіть у класах-нащадках
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)
employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)

print(john_doe.name)  # Виведе: John Doe
print(john_doe.position)  # Виведе: Manager

#___________________________________________________________________________________________

