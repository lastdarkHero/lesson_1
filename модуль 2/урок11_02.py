import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start

        print("Время работы функции {func_name} составило {total_time} сек".format(
              func_name=func.__name__, total_time = end
              ))
        
        return result
    
    return wrapper
@timer

def get_list_by_comp(val):
    return [i for i in range(val) if i % 2 == 0]

new_list = []

@timer

def get_list_by_defolt(val):
    for i in range(val):
        if i % 2 == 0:
            new_list.append(i)

get_list_by_comp(10 ** 6 *15)
get_list_by_defolt(10 ** 6 *15)

