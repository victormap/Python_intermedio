class Clase():
    def __new__(cls):
        print("new")
        return super().__new__(cls)
    def __init__(self):
        print("init")

c=Clase()