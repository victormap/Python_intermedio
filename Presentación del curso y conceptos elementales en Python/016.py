class Clase():
    def __new__(cls):
        print("new")
    def __init__(self):
        print("init")

c=Clase()