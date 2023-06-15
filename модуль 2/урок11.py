class Windows:
    def __init__(self, versions, country):
        self.__versions = versions
        self.country = country



# w = Windows(versions=10, country="China")
# print("Версия", w.__versions)
# w.__versions = 7
# print("Версия", w.__versions)

# ТАК ДЕЛАТЬ НЕ НАДО
# print("Версия", w._Windows__versions)
# w._Windows__versions = 7
# print("Версия", w._Windows__versions)