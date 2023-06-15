# def strcount(s):       # Решение за 0(N ** 2)
#     for sym in s:
#         counter = 0
#         for syb_sym in s:
#             if sym == syb_sym:
#                 counter += 1
#         print(sym, counter)

# def strcount(s):       # Решение за 0(N * M )
#     for sym in set(s):
#         counter = 0
#         for syb_sym in s:
#             if sym == syb_sym:
#                 counter += 1
#         print(sym, counter)

def strcount(s):
    my_dct = {}
    for sym in s:
        my_dct[sym] = my_dct.get(sym, 0) + 1 
    
    for sym , count in my_dct.items():
        print(sym, count)

strcount("abca")