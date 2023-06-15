class Year:
    def __init__(self):
        self.__days = 365

    @property
    def day(self):
        return self.__days
    
    @day.setter
    def day(self, days):
        if days == 365 or days == 366:
            self.__days = days
        else:
            raise ValueError(f"В году не может быть {self.__days} дней.")




year = Year()
print(year.day())
year.set_days(366)
print(year.day())
        

# _______________________________________________________________________________________________

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age

#     @property
#     def age(self):
#         return self.__age
    


#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise ValueError(f"Не допустимый возраст: {age}")
#         self.__age = age

#     @age.deleter
#     def name(self):
#         del self.__age

    
# person = Person("Жека", 14)
# print(person.age)
# person.age = 20
# print(person.age)

