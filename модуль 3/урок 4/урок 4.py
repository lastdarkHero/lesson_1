import time

# my_list = [time.sleep(x) for x in range(3)]
# my_gen = (time.sleep(x) for x in range(3))

# for item in my_gen:
#     print(item)

# def my_lazy_func():
#     for i in range(1,11):
#         print("До", i)
#         yield i 
#         print("После", i)

# for i in my_lazy_func():
#     print(i)



def my_lazy_func(items):
    for items in items:
        yield items
    yield from items

for i_items in my_lazy_func(["яблоко","банан","манго"]):
    print(i_items)