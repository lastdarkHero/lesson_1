# Арги и Кварги
# def my_func(a,b,c,*args):
#     print(a,b,c)
#     print(*args)
#     lol = args[2]
#     print(lol)
# my_func(10, 20, 30, 40, 50, 60)



# def my_fun(a,b,**kwargs):  
#    print(a,b)
#    kek = kwargs.get("d")
#    print(kek)
# my_fun(a=10,b=20,c=30,d=40,f=50)

# def mu_fen(a,b):
#     print(a,b)

# mu_fen(10 , f=20)

# def mi_fq(a,b=20):
#     print(a,b)

# mi_fq(100, 300)

# def m_q(*args,**kwargs):
#     print(args)
#     print(kwargs)

# m_q(10,20, c=30)




# Тернарный условный оператор
# age = 18

# # if age >= 18:
# #     is_allow = "можно"
# #     print(is_allow)
# # else:
# #     is_allow = "нет"
# #     print(is_allow)
# citizenship = "РФ"
# is_allow = "можно" if age >= 18 and citizenship == "РФ" else "нет"
# print(is_allow)


# Логическое присваивоние

# a= 10
# b= 20

# c = a or b

# print(c)

# c = False or b

# print(c)

# Генерация списков и словарей

my_list = []
for i in range(1001):
    if i % 5 == 0:
        my_list.append(i)
print(my_list)

my_list = [x if x % 3 == 0 else -1 for x in range(1001) if x % 5 == 0]
print(my_list)

my_dict = {x: len(x) for x in ["первый", "второй2", "третий33"] if x != "первый"}
print(my_dict)

# Сравнение по == и ID

# list_1 = [1,2]
# list_2 = [1,2]
# print(list_1 is list_2)
# print(list_1 ==  list_2)

# print(id(list_1), id(list_2))

# Кортежи

# my_tutle = tuple([1, 2, 3, 4, 5])
# # print(my_tutle)
# # my_dict = {("Евгений", "Иванов"): "+79951811830"}
# # print(my_dict)

# my_tuple = tuple(i for i in range(1001))
# print(my_tuple)




