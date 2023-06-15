class A: 
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    def __init__(self):
        pass
        
        

a1 = A()
a2 = A()
print(a1 is a2)