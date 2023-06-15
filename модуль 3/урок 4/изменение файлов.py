from contextlib import contextmanager

# file = open("text.txt", "w", encoding="utf-8")
# file.write("Вебинар")
# file.close()





# with open("text.txt", "r", encoding="utf-8") as f:
#     print(f.read())
#     print(f.closed)

# print(f.closed) 





# @contextmanager
# def revers_str(string):
#     print("входим")
#     yield string[:: -1] 
#     print("выходим")

# with revers_str("hello") as reversed_str:
#     print(reversed_str)





@contextmanager
def exc_handler(*args):
    try:
        yield True
    except args:
        print('Было исключение но мне пофик')

with exc_handler(ValueError, EncodingWarning, ArithmeticError):
    raise ValueError
