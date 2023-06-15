# Паштет 
class Animal:
    def __init__(self, name, weihgt):
        self.name = name
        self.weight = weihgt


    def  breath(self):
        print("Это животное дышит")




class Cat(Animal):
    pass



cat_1 = Cat("Паштет", 15)
cat_1.breath()
print(cat_1.weight, cat_1.name)


# Геометрические фигуры

# import abc

# class Figure(abc.ABC):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def __str__(self):
#         return f"Класс Figure. Стороны: {self.a}, {self.b}"

# class GetSqueareMixin: 
#     def get_squeare(self):
#         return self.a * self.b

# class Rectagle(Figure):
#     def __str__(self):
#         return f"Класс Rectagle. Стороны: {self.a}, {self.b}"
        
# # rect = Rectagle(10, 20)
# # print(rect)

# class Square(Figure):
#     def __init__(self, a):
#         super().__init__(a, a)
    
# def __str__(self):
#         return f"Класс Squere. Стороны: {self.a}, {self.b}"

# square = Square(10)
# print(square.get_square())