if __name__ == "__main__":

    # СОРТРОВЩИК
    goods =  [
        {
            "name": "Iphone 7",
            "brand": "Apple",
            "price": 250,
        },
        {
            "name": "Ipad",
            "brand": "Apple",
            "price": 350,
        },
        {
            "name": "Windows 7",
            "brand": "Microsoft",
            "price": 100,
        },
    ]

    def on_price(item):
        return item["price"]
        

    print(sorted(goods, key=lambda item: item["price"]))
    # --------------------------------------------------------------------------------------------
    # ФИЛЬТРОВАНИЕ

    filtered_list = list(filter(lambda item: item["brand"] == "Apple", goods))
    print(filtered_list)
    # ------------------------------------------------------------------------------------------------------
    # MAP

    numbres = ["1","2","3","4","5","6"]
    new_num = list(map(int, numbres))
    print(new_num)

    names_list = ["Егор","Сергей", "Валера"]
    surname_list = ["Новиков","X","Шмелев"]

    person_list = list(map(lambda name, surname: f"{name} {surname}", names_list, surname_list))
    print(person_list)
    # --------------------------------------------------------------------------------------------------
    # enumerate
    new_goods_list = []

    for index, item in enumerate(goods):
        new_goods_list.append({index: item})

    print(new_goods_list)
    # -------------------------------------------------------------------------------------------------
    # zip
    name_list = ["Диана","Дима", "Ирина"]
    surname_list = ["Назаров", "None", "Шишкина"]

    for name, surname in zip(name_list, surname_list):
        print(name, surname)

    print(__name__)
else:
    print("запушенно не из корня")