# Рекурсия
# def recurs(count):
#     print(count)
#     if count == 5:
#         return 
#     recurs(count + 1)
#     print(count)

# recurs(0)

# def factorial(number):
#     if number == 1:
#         return number
#     return number *factorial(number - 1)

# print(factorial(3))

# OS

# import os

# cueent_path = os.path.abspath(__file__)
# parent_patn = os.path.join(cueent_path, "..", "..")


# def get_all_path(path):
#     for i_file in os.listdir(path):
#         new_path = os.path.join(path, i_file)
#         if os.path.isdir(new_path):
#             print("Директория - ", i_file)
#             get_all_path(new_path)
#         else:
#             print(" -", i_file)


# get_all_path(parent_patn)
